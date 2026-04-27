import os
import json
from groq import Groq
from dotenv import load_dotenv
from prompts import QUIZ_PROMPT

load_dotenv()


def generate_quiz(context, num_questions):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")

    client = Groq(api_key=api_key)
    prompt = QUIZ_PROMPT.format(context=context, num_questions=num_questions)

    def attempt_generation():
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            response_format={"type": "json_object"},
        )
        return json.loads(chat_completion.choices[0].message.content)

    try:
        return attempt_generation()
    except (json.JSONDecodeError, Exception) as e:
        try:
            return attempt_generation()
        except Exception as retry_error:
            raise Exception(f"Failed to generate quiz after retry: {retry_error}")


if __name__ == "__main__":
    print(generate_quiz("front end", 5))
