# AI Content Creator(Day 49)

AI Content Creator built using **Flask** and **Google Gemini API**.

## Setup

Create virtual environment:

```powershell
python -m venv ai_content
ai_content\Scripts\activate
```

Install packages:

```powershell
pip install -r requirements.txt
```

## API Key

Copy `.env.example` to `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_real_gemini_api_key
```

Get your API key from:

https://aistudio.google.com/apikey

**Never share or upload `.env`.**

## Run

```powershell
python app.py
```

Open:

http://127.0.0.1:5000

## Features

* Text Generation
* Presentation Generation
* Image Prompt
