import feedparser
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def get_producthunt_ai_tool():

    feed = feedparser.parse("https://www.producthunt.com/feed")

    if not feed.entries:
        return "🚀 Today's AI Tool\nUnable to fetch Product Hunt tool today."

    tool_name = feed.entries[0].title

    prompt = f"""
Explain the AI tool briefly.

Tool: {tool_name}

Return:
• What it does
• Why it is useful
• One thing a developer can build with it

Keep under 50 words.
"""

    result = model.generate_content(prompt)

    return f"""🚀 Today's AI Tool
{tool_name}

{result.text}
"""