import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def generate_brief(news):

    prompt = f"""
    Create a Daily Personal AI Command Center.

    Include:

    AI Tools Mastery
    SaaS / Passive Income Experiment
    Gym Suggestion
    Reflection Question

    Here are today's news headlines:

    Tech: {news['tech']}
    Geopolitics: {news['geopolitics']}
    Indian Stock Market: {news['stocks']}
    Movies: {news['movies']}
    """

    payload = {
        "contents":[{"parts":[{"text":prompt}]}]
    }

    r = requests.post(MODEL_URL,json=payload)

    data = r.json()

    return data["candidates"][0]["content"]["parts"][0]["text"]