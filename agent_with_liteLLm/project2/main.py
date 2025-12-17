import os 
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

from agents import Agent, Runner, function_tool
from agents.extensions.models.litellm_model import LitellmModel

MODEL = 'gemini/gemini-2.0-flash'

@function_tool
def get_weather(city: str) -> str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."

agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=LitellmModel(model=MODEL, api_key = GOOGLE_API_KEY),
)

result = Runner.run_sync(agent, "What's the weather in Tokyo?")
print(result.final_output)


