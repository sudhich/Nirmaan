from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = '''
You are a professional AI content creator.

Create {content_type} content about the following topic:

{topic}

Requirements:
- Be clear and engaging.
- Match the requested content type.
- Use practical and useful information.
- Do not invent specific facts.
- Return only the requested content.
'''

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json() or {}
        topic = (data.get("topic") or "").strip()
        content_type = data.get("content_type", "LinkedIn Post")

        if not topic:
            return jsonify({"success": False, "error": "Please enter a topic."}), 400

        if not os.getenv("OPENAI_API_KEY"):
            return jsonify({"success": False, "error": "OPENAI_API_KEY is not set."}), 500

        prompt = PROMPT.format(content_type=content_type, topic=topic)

        response = client.responses.create(
            model="gpt-5.6-mini",
            input=prompt
        )

        return jsonify({
            "success": True,
            "content": response.output_text
        })

    except Exception as exc:
        return jsonify({"success": False, "error": str(exc)}), 500

if __name__ == "__main__":
    app.run(debug=True)
