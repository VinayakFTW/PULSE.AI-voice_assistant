from fastapi import FastAPI
import uvicorn

from backend.pulse_models.response_model import AgentResponse
from backend.pulse_controllers.core_chat_controllers.chat_controller import process_chat
from backend.pulse_controllers.whatsapp_chat_controllers.send_wa_text import openwa_webhook

app = FastAPI(title="PulseAI Server", description="API server for PulseAI backend")


app.add_api_route("/api/v1/chat",
                  process_chat,
                  methods=["POST"], 
                  response_model=AgentResponse, 
                  summary="Process chat requests"
                  )

app.add_api_route("/api/v1/whatsapp/webhook",
                  openwa_webhook,
                  methods=["POST"],
                  summary="Webhook for receiving WhatsApp messages"
                  )

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)