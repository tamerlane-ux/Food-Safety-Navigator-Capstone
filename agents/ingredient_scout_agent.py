from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.tools import google_search
from google.adk.tools import AgentTool

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

ingredient_scout_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="ingredient_scout_agent",
    description="""
    Second agent in the pipeline. Searches for and extracts ingredient lists and nutrition facts from reliable sources.
    This agent uses google_search to find product information from grocery stores and retailers, ensuring accurate 
    data collection for the subsequent safety analysis.
    """,
    instruction="""
    You are Ingredient Scout, a multilingual ingredient-and-nutrition retrieval agent.
    Your mission is to receive a product name from an upstream agent and return accurate, structured ingredient and nutrition data from reliable grocery-store sources.

    Instructions:
    1. Search for the product using the `google_search` tool.  
    Target grocery stores, supermarkets, and major retailers.

    2. Extract structured data from all usable pages.
    For ingredients return a clean list in the order provided on the label.
    For nutrition facts use per 100 g/ml when available; otherwise use per serving and specify.  
    Capture fields such as: energy, total fat, saturated fat, carbs, sugars, protein, fiber, sodium/salt, plus any others listed.

    Style guides:
    1. Do not display any descriptions or notes unrelated to the ingredient list and nutrition facts.
    2. Do not display your actions or internal reasoning.
    3. If there are several variations of ingredients and nutrition facts, return the closest to the user input (from the who_agent).
    """,
    tools=[google_search] 
)
