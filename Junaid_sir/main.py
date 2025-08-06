from json import load
import os
# import chainlit as cl
from agents import Agent, Tool, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner


from dotenv import load_dotenv

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",

)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,

)
run_config = RunConfig(
    model=model,
    tracing_disabled=True
)

agent1 = Agent(
    name="Panaversity support agent",
    instructions="You are a helpful assisstent"
)
result = Runner.run_sync(
    input="What is the capital of France?",
    run_config=run_config,
    starting_agent=agent1   
)
print(result)








# @cl.on_message
# async def main(message: cl.Message):
#     # Our custom logic goes here...
#     # Send a fake response back to the user
#     await cl.Message(
#         content=f"Received: {message.content}",
#     ).send()