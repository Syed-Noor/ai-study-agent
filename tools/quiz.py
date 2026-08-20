def create_quiz_prompt(topic: str, number: int):

    return f"""
Create {number} multiple-choice questions about:

{topic}

Requirements:

- Four options per question
- Clearly identify the correct answer
- Include a short explanation
- Difficulty should be suitable for a university computer science student
"""