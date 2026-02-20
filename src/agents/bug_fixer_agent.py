from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from services.agent_instructions_service import get_agent_instruction_by_name
from .git_master_agent import git_master_agent
from tools.notification_tool import notification_tool

bug_fixer_agent = Agent(
    name="bug_fixer_agent",
    description="Fixes all the code related issues, creates code commits and raises pull requests",
    instruction=(get_agent_instruction_by_name("bug_fixer_agent")),
    tools=[AgentTool(git_master_agent), notification_tool],
    # input_schema=
    # output_schema=
)
