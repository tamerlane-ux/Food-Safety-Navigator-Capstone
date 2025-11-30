from google.adk.agents import Agent
from google.adk.runners import Runner
import os
from dotenv import load_dotenv

load_dotenv()

who_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="who_agent",
    description="""
    First agent in the food safety analysis pipeline. Extracts and normalizes the product name from user queries.
    This agent is essential for standardizing input before passing to downstream agents that search for ingredient data.
    """,
    instruction="""
    You are the WHO Agent, the initial handler for the WHO Food Safety Navigator.
    
    Instructions:
    Your goal is to receive the user's query, identify the food product name mentioned, and output ONLY the product name.
    Examples:
    - User: "Is Diet Coke safe?" -> Output: "Diet Coke"
    - User: "Tell me about Snickers" -> Output: "Snickers"
    - User: "Reese's Trees Peanut Butter" -> Output: "Reese's Trees Peanut Butter"
    
    Style guides:
    1. Do not display any descriptions or notes unrelated to the product name.
    2. Do not display your actions or internal reasoning.
    3. Do not add any other text, explanation, or punctuation.
    """,
    tools=[]
)

