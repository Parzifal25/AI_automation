import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_insights():

    prompt = """
    Generate a short daily AI briefing.

    Return:

    1. One AI tool that a developer/AI enthusiast should learn today.
    Include:
    - tool name
    - what it does
    - one practical thing to build with it.

    2. One realistic AI micro SaaS idea for India that can make passive income.
    Include:
    - idea name
    - what problem it solves
    - who will pay for it.

    Keep it concise.
    """

    response = model.generate_content(prompt)

    return response.text