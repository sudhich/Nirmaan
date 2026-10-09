# Prompt Engineering Portfolio — Gemini API

A Day 50 practical portfolio covering prompt-engineering techniques and three Gemini-powered applications.

## Portfolio sections

1. Zero-Shot Prompting
2. Few-Shot Prompting
3. Role Prompting
4. Structured Output
5. Prompt Optimization
6. Resume Analyzer
7. Customer Support Assistant
8. AI Content Creator

## Requirements

- Python 3.10+
- A Gemini API key

## Setup on Windows PowerShell

```powershell
python -m venv portfolio
portfolio\Scripts\activate
pip install -r requirements.txt
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Run an application:

```powershell
cd 06_resume_analyzer
python app.py
```

Then open the local URL shown by Flask.

For the other applications, use the same pattern:

```powershell
cd ..\07_customer_support
python app.py
```

or:

```powershell
cd ..\08_ai_content_creator
python app.py
```

## Security

Never put your real API key in source code or commit it to GitHub.
Use an environment variable or a local `.env` file.
