from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class ExceptionDetails(BaseModel):
    type: str
    message: str
    module: str
    line_number: int = Field(alias="line_number")
    file: str
    stack_trace: List[str] = Field(alias="stack_trace")


class LogMetadata(BaseModel):
    container_id: str = Field(alias="container_id")
    region: str
    shard: str
    cpu_usage: str = Field(alias="cpu_usage")
    memory_usage: str = Field(alias="memory_usage")


class LogEntry(BaseModel):
    app: str
    timestamp: datetime
    level: str
    logger: str
    request_id: str = Field(alias="request_id")
    request_path: str = Field(alias="request_path")
    method: str
    user_agent: str = Field(alias="user_agent")
    exception: ExceptionDetails
    metadata: LogMetadata
