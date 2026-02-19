import os

from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp.client.stdio import StdioServerParameters
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from dotenv import load_dotenv
from services.agent_instructions_service import get_agent_instruction_by_name

load_dotenv()

github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
try:
    connection_params = StdioConnectionParams(
        server_params=StdioServerParameters(
            command="docker",
            args=[
                "run",
                "-i",
                "--rm",
                "-e",
                f"GITHUB_PERSONAL_ACCESS_TOKEN={github_token}",
                "ghcr.io/github/github-mcp-server",
            ],
        )
    )

    git_master_agent = Agent(
        name="git_master_agent",
        model="gemini-2.5-flash",
        instruction=(get_agent_instruction_by_name("git_master_agent")),
        tools=[McpToolset(connection_params=connection_params)],
    )
except Exception as e:
    raise e
