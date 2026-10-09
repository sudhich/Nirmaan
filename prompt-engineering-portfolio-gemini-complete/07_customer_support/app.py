from pathlib import Path
import sys
from flask import Flask, request, render_template_string

sys.path.append(str(Path(__file__).resolve().parent.parent))
from gemini_client import generate
from prompts import SUPPORT_PROMPT

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
<title>Gemini Customer Support</title>
<style>
body{font-family:Arial;max-width:900px;margin:40px auto;padding:20px}
textarea{width:100%;height:180px;padding:12px}
button{padding:12px 22px;margin-top:12px}
pre{white-space:pre-wrap;background:#f5f5f5;padding:20px}
</style>
</head>
<body>
<h1>Gemini Customer Support Assistant</h1>
<form method="post">
<textarea name="message" placeholder="Enter customer message...">{{ message }}</textarea>
<br><button type="submit">Generate Response</button>
</form>
{% if result %}<h2>Suggested Response</h2><pre>{{ result }}</pre>{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    result = ""
    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if message:
            try:
                result = generate(SUPPORT_PROMPT.format(message=message))
            except Exception as e:
                result = f"Error: {e}"
    return render_template_string(HTML, message=message, result=result)

if __name__ == "__main__":
    app.run(debug=True)
