# Structured Output

Structured prompting asks the model to return information in a predictable format.

## JSON-style output

```text
Extract information from this job description.

Return ONLY valid JSON using this structure:

{
  "job_title": "",
  "skills": [],
  "experience_required": "",
  "location": ""
}

Job description:
Python Developer with 2 years of experience...
```

## Table output

```text
Compare Python, Java, and JavaScript.

Return a Markdown table with these columns:
Language | Main Use | Difficulty | Example Application
```

## Checklist output

```text
Create a 5-step checklist for deploying a Flask application.
Return exactly 5 numbered steps.
```
