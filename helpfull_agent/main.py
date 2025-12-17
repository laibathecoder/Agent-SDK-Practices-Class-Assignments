
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment not found please set it in the .env file")

external_client = AsyncOpenAI(
    api_key = OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-r1-0528:free",
    openai_client=external_client
)

set_tracing_disabled(True)

agent = Agent(
    name="Helpful Assistant",
    instructions="You are a helpful assistant that provides accurate and friendly responses.",
    model = model  
)


# One Time Responce
# output = Runner.run_sync(
#     starting_agent = agent,
#     input="Hello, I'm a helpful assistant"
# )

# print(output.final_output)



# Using while loop for get user input and make iteration again and again

while True:
    user_input = input("How can i help you? (q for 'Quit')")
    if user_input.lower() == "q":
        print("Program is closing...")
        break
    else:
        if user_input.strip() == "":
            print("Please write something.")
            continue

    try:
        output = Runner.run_sync(
            starting_agent = agent , 
            input = user_input
        )

        print("Assistant Answer: " , output.final_output)

    except Exception as e :
        print("Error: " , str(e))

print("Thanks for using the assistant!") 