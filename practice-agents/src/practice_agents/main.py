
import os 
from dotenv import load_dotenv
from agents import Agent , Runner , AsyncOpenAI , OpenAIChatCompletionsModel , set_tracing_disabled
load_dotenv()



os.getenv = GOOGLE_API_KEY = ("GOOGLE_API_KEY")

external_client = AsyncOpenAI(
    api_key = GOOGLE_API_KEY ,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
    
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

set_tracing_disabled = True   


agent = Agent(
    name = "helpfull assistant",
    instructions = "You are a helpfull asistant"
)

output = Runner.run_sync(starting_agent = agent , input = "Hello i'm a helpfull assistant")
print(output.final_output)
