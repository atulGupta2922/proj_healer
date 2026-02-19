import os

from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp.client.stdio import StdioServerParameters
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from dotenv import load_dotenv

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

    root_agent = Agent(
        name="root_agent",
        model="gemini-2.5-flash",
        instruction=(get_agent_instruction_by_name("root_agent")),
        tools=[McpToolset(connection_params=connection_params)],
    )
except Exception as e:
    raise e
