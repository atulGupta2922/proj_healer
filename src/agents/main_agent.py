from google.adk.agents.llm_agent import Agent
from services.agent_instructions_service import get_agent_instruction_by_name
from schemas.main_agent_input_schema import LogEntry
from schemas.rca_agent_input_schema import RcaAgentInput

try:
    main_agent = Agent(
        name="main_agent",
        model="gemini-2.5-pro",
        instruction=(get_agent_instruction_by_name("main_agent")),
        input_schema=LogEntry,
        output_schema=RcaAgentInput,
    )
except Exception as e:
    raise e
