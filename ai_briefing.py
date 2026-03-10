from news_fetcher import fetch_news
from ai_insights import generate_ai_insights
from ai_tool_finder import get_producthunt_ai_tool
from datetime import datetime


def generate_ai_briefing():

    news = fetch_news()
    insights = generate_ai_insights()
    ai_tool = get_producthunt_ai_tool()

    today = datetime.now().strftime("%d %B %Y")

    briefing = f"""📊 AI COMMAND CENTER
    Date: {today}

    {ai_tool}

    🤖 AI DAILY INSIGHT
    {insights}

    🏋️ Gym
    Push Day
    • Pushups – 3 sets
    • Chest press – 4 sets
    • Triceps dips – 3 sets

    {news}

    🧠 Reflection
    What did I build today?
    """

    return briefing