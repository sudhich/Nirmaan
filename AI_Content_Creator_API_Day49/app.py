from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

app = Flask(__name__)

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to .env")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Gemini model
MODEL = "gemini-3.5-flash-lite"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json() or {}

        topic = (data.get("topic") or "").strip()
        content_type = data.get("content_type", "Text")

        # Check topic
        if not topic:
            return jsonify({
                "success": False,
                "error": "Please enter a topic."
            }), 400

        # Create prompt
        if content_type == "Text":

            prompt = f"""
            Create high-quality educational content about:

            {topic}

            Use simple English.
            Include:
            - A clear title
            - Introduction
            - Headings
            - Bullet points where useful
            - Practical examples
            """

        elif content_type == "Presentation":

            prompt = f"""
            Create a 10-slide presentation about:

            {topic}

            For every slide provide:
            - Slide title
            - 3 to 5 concise bullet points
            """

        elif content_type == "Image":

            prompt = f"""
            Create a detailed AI image-generation prompt based on:

            {topic}

            Include:
            - Subject
            - Environment
            - Composition
            - Lighting
            - Visual style
            - Important details
            - Aspect ratio
            """

        else:

            return jsonify({
                "success": False,
                "error": "Invalid content type."
            }), 400

        # Generate content using Gemini
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        # Return generated text
        return jsonify({
            "success": True,
            "content": response.text
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
