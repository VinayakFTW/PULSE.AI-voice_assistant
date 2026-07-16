from pydantic import BaseModel

class UserRequest(BaseModel):
    query: str
    user_id: str = "default_user"
    channel: str = "default_channel"
