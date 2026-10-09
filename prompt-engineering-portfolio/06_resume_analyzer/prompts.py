RESUME_PROMPT = '''
You are an expert technical recruiter.

Analyze the resume below.

Return the analysis using these sections:
1. Candidate Name
2. Technical Skills
3. Years of Experience
4. Education
5. Strengths
6. Missing or Recommended Skills
7. Suitable Job Roles
8. Improvement Suggestions

Rules:
- Base the answer only on information present in the resume.
- Do not invent qualifications or experience.
- If information is missing, say "Not specified".
- Be concise and professional.

Resume:
{resume}
'''
