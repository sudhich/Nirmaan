RESUME_PROMPT = """
You are an expert resume reviewer for entry-level AI, Data Science, and Python roles.

Analyze the resume below.

Return these sections:
1. Overall summary
2. Strong skills
3. Missing or weak areas
4. Suggested project improvements
5. ATS keyword suggestions
6. Three concrete next steps

Be honest, specific, and beginner-friendly.

RESUME:
{resume}
"""
