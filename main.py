# Imports for asynchronous operations and OS interaction
import asyncio
import os

# Third-party library for loading environment variables
from dotenv import load_dotenv

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
import google.genai.types as types
from google.adk.agents import SequentialAgent

# Local agent imports for specific functionalities
from agents.who_agent import who_agent
from agents.ingredient_scout_agent import ingredient_scout_agent
from agents.verdict_vector_agent import verdict_vector_agent

# Loading environment variables
load_dotenv()

# Configuring Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found. Please check your .env file.")

async def main():
    """
    Main entry point for WHO Food Safety Navigator.

    """
    # Get user input for the food product query
    print("=" * 60)
    print("\nWHO Food Safety Navigator 🌐")
    print("=" * 60)
    user_query = input("\nEnter the food product you want to analyze in details: ").strip()
    
    if not user_query:
        print("❌ No query provided. Exiting...")
        return
    
    print(f"\n🔍 Analyzing: {user_query}")
    print("-" * 60)
    
    try:
        # Create an in-memory session service for testing
        session_service = InMemorySessionService()
        
        # Create the sequential agent
        root_agent = SequentialAgent(
            name="AnalysisPipiline",
            sub_agents=[who_agent, ingredient_scout_agent, verdict_vector_agent],
        )
        
        # Create a runner for the WHO agent with session service
        runner = Runner(
            app_name="agents",
            agent=root_agent,
            session_service=session_service
        )
        
        # Create a session for the user
        user_id = "test_user"
        session_id = "test_session_001"
        
        await session_service.create_session(
            app_name="agents",
            user_id=user_id,
            session_id=session_id
        )
        
        # Create a message content
        message = types.Content(
            role="user",
            parts=[types.Part(text=user_query)]
        )
        
        # Run the agent and process events
        print("\n⏳ Processing your request... (This may take a moment)")
        events = runner.run(
            user_id=user_id,
            session_id=session_id,
            new_message=message
        )
        
        # Collect all events and display only the final response from verdict_vector_agent
        all_events = list(events)
        
        if all_events:
            final_event = all_events[-1]
            if hasattr(final_event, 'content') and final_event.content:
                print("\n" + "=" * 60)
                print("\n FOOD SAFETY ANALYSIS RESULT 🔍")
                print("=" * 60 + "\n")
                for part in final_event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        print(part.text)
                print("\n" + "=" * 60)
        else:
            print("No response received from agents.")
    # Error display    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

# Ensures that main() is called only when the script is executed directly, not when imported as a module.
if __name__ == "__main__":
    asyncio.run(main())
