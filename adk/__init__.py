class Gemini:
    def __init__(self, model: str, retry_options=None):
        self.model_name = model
        self.retry_options = retry_options

class LlmAgent:
    def __init__(self, model, name: str, instruction: str, tools: list = None):
        self.model = model
        self.name = name
        self.instruction = instruction
        self.tools = tools or []

    async def process_request(self, user_query: str):
        # Simulation of processing
        return f"[{self.name}] Processed: {user_query}"
