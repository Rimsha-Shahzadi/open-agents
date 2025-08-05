from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, ModelSettings, RunContextWrapper, FunctionTool
# from agents.agent import StopAtTools
from typing import Any
# from typing import FunctionArgs
# from dis import Instruction
# from openai import AsyncOpenAI
from pydantic import BaseModel, ConfigDict
from dotenv import load_dotenv
import os

load_dotenv()
def do_some_work(dara: str) -> str:
    return "done"
class FunctionArgs(BaseModel):
    username: str
    age: int
    model_config = ConfigDict(extra="forbid")
async def run_function_tool(ctx: RunContextWrapper[Any], args: str) -> str:
    print("args type print",type (args))
    print("args print", args)
    parsed = FunctionArgs.model_validate_json(args)
    return "My fun run ! woo"

tool = FunctionTool(
    name="process_user",
    description="Process extracted user data",
    params_json_schema=FunctionArgs.model_json_schema(),
    on_invoke_tool=run_function_tool
)
# GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
# class Addparam(BaseModel):
#     a: int
#     b: int

# @function_tool(name_override="addition", description_override="Addition two Numbers")
# async def add(params: Addparam) -> str:
#     """Add two numbers"""
#     print("Add called")
#     return params.a + params.b 

# @function_tool()
# def human_review():
#     """human review in the loop"""
#     print("human review called")
#     return "human in the loop call"

# client = AsyncOpenAI(
#     api_key=GOOGLE_KEY,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )
agent = Agent(name="basic_agent",
    instructions="You are a basic agent that can execute simple Python code.",
    # model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    tools=[tool],
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["human_review"]),
    # model_settings=ModelSettings(tool_choice="required"),
    # reset_tool_choice=False,
    )
# query = ("process user data, Miss Rimsha, 22 years old")
# print(agent.tools)
# result = Runner.run_sync(agent, query)
# print(result.final_output)
print(agent.tools)
output= Runner.run_sync(agent, input="process user data, Miss Rimsha, 22 years old")
print(output.final_output)




   