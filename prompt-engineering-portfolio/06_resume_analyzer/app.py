from flask import Flask, request, render_template_string
import os
from openai import OpenAI
from prompts import RESUME_PROMPT

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HTML = '''
<!doctype html>
<html>
<head>
<title>AI Resume Analyzer</title>
<style>
body{font-family:Arial;background:#f4f7fb;margin:0;padding:40px}
.card{max-width:900px;margin:auto;background:white;padding:30px;border-radius:16px;box-shadow:0 8px 30px #0001}
textarea{width:100%;height:280px;padding:12px;box-sizing:border-box}
button{margin-top:15px;padding:12px 22px;border:0;border-radius:8px;background:#2563eb;color:white;cursor:pointer}
pre{white-space:pre-wrap;background:#f7f7f7;padding:20px;border-radius:10px}
</style>
</head>
<body>
<div class="card">
<h1>AI Resume Analyzer</h1>
<p>Paste a resume below and generate an AI-powered analysis.</p>
<form method="post">
<textarea name="resume" placeholder="Paste resume text here...">{{ resume }}</textarea>
<br><button type="submit">Analyze Resume</button>
</form>
{% if result %}
<h2>Analysis</h2><pre>{{ result }}</pre>
{% endif %}
{% if error %}<p style="color:#c00">{{ error }}</p>{% endif %}
</div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    resume = ""
    result = ""
    error = ""

    if request.method == "POST":
        resume = request.form.get("resume", "").strip()
        if not resume:
            error = "Please paste a resume."
        elif not os.getenv("OPENAI_API_KEY"):
            error = "OPENAI_API_KEY is not set."
        else:
            try:
                response = client.responses.create(
                    model="gpt-5.6-mini",
                    input=RESUME_PROMPT.format(resume=resume)
                )
                result = response.output_text
            except Exception as exc:
                error = f"API error: {exc}"

    return render_template_string(HTML, resume=resume, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
