from pydantic import BaseModel


class RcaAgentInput(BaseModel):
    error_message: str
    line_number: int
    filename: str
    impacted_files_trace: list[str]
    issue_description: str
