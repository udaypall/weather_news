
import asyncio
import os

from ddgs import DDGS
from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


# Load API key
load_dotenv()


# Search tool
def search_weather_news(city: str) -> str:
    """
    Search DuckDuckGo News for today's weather
    news and forecasts for the specified city.

    Return up to five news articles containing
    headlines, descriptions, dates and sources.
    """

    try:
        results = DDGS().news(
            query=f"{city} weather today",
            max_results=5
        )

        return str(results)

    except Exception as e:
        return f"Search failed: {str(e)}"


# Get city from user
city = input("Which city? ").strip()

if not city:
    raise SystemExit("Please enter a city.")


# OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not found.")


# Create OpenAI client
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=api_key
)


# Create AutoGen agent
agent = AssistantAgent(
    name="weather_news",
    model_client=model_client,
    tools=[search_weather_news],

    system_message="""
    You are an intelligent Weather News Assistant.

    Always use the search_weather_news tool
    to retrieve weather news for the requested city.

    Analyze the search results using your intelligence.

    Your responsibilities:

    1. Identify relevant weather-related information.
    2. Ignore unrelated news articles.
    3. Identify current weather conditions.
    4. Summarize rainfall, temperature and forecasts.
    5. Identify important weather alerts.
    6. Never invent weather information.
    7. If relevant information is unavailable,
       clearly mention that it could not be verified.

    FINAL RESPONSE:

        - 🌦️ Weather: Current weather conditions.
        - 🌧️ Forecast: Rainfall and weather alerts.
        - ⚠️ Advisory: Relevant safety advice.

    Return exactly three short bullet points.
    Keep the response clear and concise.
    """,

    reflect_on_tool_use=True
)


# Run agent
async def main():

    try:
        print("\nStarting Weather News Agent...\n")

        await Console(
            agent.run_stream(
                task=f"Find today's weather news for {city}."
            )
        )

    finally:
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
