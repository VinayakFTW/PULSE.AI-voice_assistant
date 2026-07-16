from pydantic import BaseModel

class AgentResponse(BaseModel):
    success: bool
    response: str
    tool_result: str = None
