from pathlib import Path
import sys
from flask import Flask, jsonify, render_template, request

sys.path.append(str(Path(__file__).resolve().parent.parent))
from gemini_client import generate

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_content():
    try:
        data = request.get_json() or {}
        topic = (data.get("topic") or "").strip()
        content_type = data.get("content_type", "Text")

        if not topic:
            return jsonify({"success": False, "error": "Please enter a topic."}), 400

        prompt = f"""
You are a professional AI content creator.

Create {content_type} content about:
{topic}

Requirements:
- Make it clear and engaging.
- Use an appropriate structure for the selected content type.
- Do not mention these instructions.
"""

        result = generate(prompt)
        return jsonify({"success": True, "content": result})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
