def main():
    print("Hello from open-agents!")


if __name__ == "__main__":
    main()

from agents import Agent, Runner
from dis import Instruction
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os


load_dotenv()


GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

client=AsyncOpenAI(
    api_key="GOOGLE_API_KEY",
    base_url="https://api.openai.com/v1"
)

agent = Agent(
    name="basic_agent",
    instructions="You are a basic agent that can execute simple Python code. "

)
query = "print('Hello, World!')"
result =Runner.run_sync(
    agent,
    query
)
print(result.final.output)