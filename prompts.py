QUIZ_PROMPT = """You are a quiz generator. Given the following text extracted from a document, generate {num_questions} multiple choice questions.

Rules:
- Each question must be directly answerable from the text
- 4 answer choices per question (A, B, C, D)
- Only one correct answer per question
- Choices must be plausible, not obviously wrong
- Do not use phrases like "according to the text" or "the passage states"
- Questions should test understanding, not just copy-paste from the text

Text:
{context}

Respond ONLY in this JSON format, no preamble, no markdown:
{{
  "questions": [
    {{
      "question": "...",
      "choices": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
      "answer": "A",
      "explanation": "Brief explanation of why this is correct"
    }}
  ]
}}"""
