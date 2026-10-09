from pathlib import Path
import sys
from flask import Flask, request, render_template_string

sys.path.append(str(Path(__file__).resolve().parent.parent))
from gemini_client import generate
from prompts import RESUME_PROMPT

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
<title>Gemini Resume Analyzer</title>
<style>
body{font-family:Arial;max-width:900px;margin:40px auto;padding:20px}
textarea{width:100%;height:300px;padding:12px}
button{padding:12px 22px;margin-top:12px}
pre{white-space:pre-wrap;background:#f5f5f5;padding:20px}
</style>
</head>
<body>
<h1>Gemini Resume Analyzer</h1>
<p>Paste your resume and get structured improvement suggestions.</p>
<form method="post">
<textarea name="resume" placeholder="Paste your resume here...">{{ resume }}</textarea>
<br><button type="submit">Analyze Resume</button>
</form>
{% if result %}<h2>Analysis</h2><pre>{{ result }}</pre>{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resume = ""
    result = ""
    if request.method == "POST":
        resume = request.form.get("resume", "").strip()
        if resume:
            try:
                result = generate(RESUME_PROMPT.format(resume=resume))
            except Exception as e:
                result = f"Error: {e}"
    return render_template_string(HTML, resume=resume, result=result)

if __name__ == "__main__":
    app.run(debug=True)
