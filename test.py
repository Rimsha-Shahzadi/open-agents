from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, ModelSettings
from agents.agent import StopAtTools
from dis import Instruction
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

@function_tool()
def add(a: int, b: int) -> str:
    """Add two numbers"""
    print("Add called")
    return a + b -5

@function_tool()
def human_review():
    """human review in the loop"""
    print("human review called")
    return "human in the loop call"

client = AsyncOpenAI(
    api_key=GOOGLE_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
agent = Agent(name="basic_agent",
    instructions="You are a basic agent that can execute simple Python code.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    tools=[add, human_review],
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["human_review"]),
    model_settings=ModelSettings(tool_choice="required"),
    reset_tool_choice=False
    )
query = "Hi"
result = Runner.run_sync(agent, query)
print(result.final_output)