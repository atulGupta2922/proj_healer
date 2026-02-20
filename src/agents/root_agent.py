import json
import os

from google.adk.agents.sequential_agent import SequentialAgent
from google.genai import types
from google.adk.runners import InMemoryRunner
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from services.agent_instructions_service import get_agent_instruction_by_name
from dotenv import load_dotenv
from agents.main_agent import main_agent
from agents.rca_agent import rca_agent
from agents.bug_fixer_agent import bug_fixer_agent


load_dotenv()

try:
    root_agent = SequentialAgent(
        name="root_agent",
        description="Runs the Code healer Agents in sequence.",
        sub_agents=[main_agent, rca_agent, bug_fixer_agent],
    )
except Exception as e:
    raise e


async def trigger_agent(alert_payload):
    if not os.getenv("GOOGLE_API_KEY"):
        raise RuntimeError("GOOGLE_API_KEY environment variable is not set")
    # 1. Create runner
    runner = InMemoryRunner(
        agent=root_agent,
        app_name="healer",
    )
    # 2. Create a Session
    # Sessions maintain conversation history/state.
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="local-user"
    )
    # 3. Init Trigger Prompt (User Input)
    prompt = json.dumps(alert_payload)
    print(f"--- Triggering Agent with prompt: '{prompt}' ---")
    # 4. We construct a user message and iterate through the event stream.
    user_message = types.Content(role="user", parts=[types.Part(text=prompt)])
    # Collect the model's textual reply
    reply_chunks: list[str] = []
    # 5. Run the Agent
    async for event in runner.run_async(
        user_id=session.user_id, session_id=session.id, new_message=user_message
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                text = getattr(part, "text", None)
                if text:
                    reply_chunks.append(text)
    if reply_chunks:
        # Join all text parts for this turn
        reply_text = "".join(reply_chunks)
        print(f"Agent: {reply_text}\n")
    else:
        print("Agent: (no response content received)\n")
    return reply_text
