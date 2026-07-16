from pydantic import BaseModel

class UserRequest(BaseModel):
    query: str
    user_id: str
    channel: str = "default_channel"
