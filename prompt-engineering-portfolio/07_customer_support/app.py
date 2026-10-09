from flask import Flask, request, render_template_string
import os
from openai import OpenAI
from prompts import SUPPORT_PROMPT

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HTML = '''
<!doctype html>
<html>
<head>
<title>AI Customer Support</title>
<style>
body{font-family:Arial;background:#eef2ff;padding:40px}
.card{max-width:800px;margin:auto;background:white;padding:30px;border-radius:16px}
textarea{width:100%;height:180px;padding:12px;box-sizing:border-box}
button{margin-top:15px;padding:12px 22px;border:0;border-radius:8px;background:#4f46e5;color:white}
pre{white-space:pre-wrap;background:#f5f5f5;padding:18px;border-radius:10px}
</style>
</head>
<body>
<div class="card">
<h1>AI Customer Support Assistant</h1>
<form method="post">
<textarea name="message" placeholder="Example: My order hasn't arrived yet.">{{ message }}</textarea>
<br><button>Get Support Response</button>
</form>
{% if result %}<h2>Response</h2><pre>{{ result }}</pre>{% endif %}
{% if error %}<p style="color:red">{{ error }}</p>{% endif %}
</div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    result = ""
    error = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if not message:
            error = "Please enter a customer message."
        elif not os.getenv("OPENAI_API_KEY"):
            error = "OPENAI_API_KEY is not set."
        else:
            try:
                response = client.responses.create(
                    model="gpt-5.6-mini",
                    input=SUPPORT_PROMPT.format(message=message)
                )
                result = response.output_text
            except Exception as exc:
                error = f"API error: {exc}"

    return render_template_string(HTML, message=message, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
