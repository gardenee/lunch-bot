import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
from langchain_mcp_adapters.tools import load_mcp_tools

load_dotenv()


def get_model():
    ''' 모델 기본 설정 '''
    return ChatOpenAI(
        model="gpt-4o",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        max_tokens=None,
        timeout=None,
        temperature=0.7,
        top_p=0.9
    )


async def run_agent(user_prompt: str):
    ''' 에이전트 실행 '''
    server_params = StdioServerParameters(
        command="python",
        args=["/Users/garden/Documents/lunch-bot/app/mcp/lunch_bot.py"],
        transport="stdio"
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)

            agent = create_react_agent(get_model(), tools)
            agent_response = await agent.ainvoke({"messages": user_prompt})

        return agent_response
