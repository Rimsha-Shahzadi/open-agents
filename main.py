def main():
    print("Hello from open-agents!")


if __name__ == "__main__":
    main()

from agents import Agent, Runner,  OpenAIChatCompletionsModel
from dis import Instruction
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()


GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


client=AsyncOpenAI(
    api_key=GOOGLE_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

agent = Agent(
    name="basic_agent",
    instructions="You are a basic agent that can execute simple Python code. ",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),

)
query = "What is the Capital Of Pakistan?"


result =Runner.run_sync(
    agent,
    query
)

print(result.final_output)