from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from services.agent_instructions_service import get_agent_instruction_by_name
from .git_master_agent import git_master_agent
from schemas.rca_agent_input_schema import RcaAgentInput
from tools.notification_tool import notification_tool
from tools.git_custom_tools import get_repository_name_by_app_name

rca_agent = Agent(
    name="rca_agent",
    description="",
    instruction=(get_agent_instruction_by_name("rca_agent")),
    tools=[
        AgentTool(git_master_agent),
        notification_tool,
        get_repository_name_by_app_name,
    ],
    input_schema=RcaAgentInput,
    # output_schema=
)
