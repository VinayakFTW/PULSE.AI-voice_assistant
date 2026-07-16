from backend.pulse_models.request_model import UserRequest
from backend.pulse_helpers.postgre_helpers import get_user_by_phone,create_user

import os
from dotenv import load_dotenv

load_dotenv()

def validate_user(req: UserRequest):
    """
    Dependency to check if the user exists before processing the chat.
    """
    if os.getenv("MODE") == "development":
        # In development mode, use random number configure in your .env
        req.phone_number = os.getenv("MOCK_NUM")

    user = get_user_by_phone(req.phone_number)
    
    if not user:
        user = create_user(req.phone_number)

    return user