import os
import httpx
from fastapi import BackgroundTasks, Request

from backend.pulse_controllers.core_chat_controllers.chat_controller import process_chat
from backend.pulse_models.request_model import UserRequest
from backend.pulse_models.response_model import AgentResponse
from backend.pulse_controllers.openwa_controllers.resolve_chat_id_to_phone import resolve_chat_id_to_phone
from backend.pulse_controllers.openwa_controllers.get_wa_session import get_wa_session_id

OPENWA_URL = os.getenv("OPENWA_URL")
OPENWA_API_KEY = os.getenv("OPENWA_API_KEY")

async def process_and_reply(sender_id: str, phone_number: str, message_body: str, response_text: str):
    """
    Background task to run the LLM orchestrator and send the reply back via OpenWA.
    """
    req = UserRequest(phone_number=phone_number, query=message_body, channel="whatsapp")

    response_text = process_chat(req)

    url = f"{OPENWA_URL}/api/sessions/{get_wa_session_id()}/messages/send-text"
    payload = {
        "chatId": sender_id,
        "text": response_text, 
    }
    
    headers = {
        "X-API-Key": OPENWA_API_KEY,
    }
    
    async with httpx.AsyncClient() as client:
        try:
            await client.post(url, json=payload, headers=headers)
            return AgentResponse(success=True,
                                response=response_text, 
                                )
        except Exception as e:
            return AgentResponse(success=False,
                                response=f"Failed to send WhatsApp message: {str(e)}", 
                                )

async def openwa_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Controller logic to handle incoming OpenWA messages.
    """
    payload = await request.json()
    
    event = payload.get("event")
    data = payload.get("data", {})

    if event == "message.received" and not data.get("isGroupMsg", False):
        if data.get("fromMe", False):
            return {"status": "ignored_self_message"}
        sender_id = data.get("from")
        message_body = data.get("body")
        
        if sender_id and message_body:
            phone_number = await resolve_chat_id_to_phone(session_id=get_wa_session_id(), chat_id=sender_id)
            
            background_tasks.add_task(process_and_reply, sender_id, phone_number, message_body)

    return {"status": "received"}