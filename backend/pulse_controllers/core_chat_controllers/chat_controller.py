from backend.pulse_config.prompts import tool_system_prompt
from backend.pulse_brain.llm_interface import tool_dispatcher,load_model,generate_response
from backend.pulse_brain.memory import load_history, save_history
from backend.pulse_models.request_model import UserRequest

from fastapi import HTTPException

async def process_chat(request: UserRequest):
    try:
        client = load_model()
        conversation_history = load_history()
        listening = True
        if listening:
            query = request.query
            if not query or query == "0":
                listening = False
                return {"success": False, "message": "No query provided."}
             
            tool_check_history = [{"role": "system", "content": tool_system_prompt}, {"role": "user", "content": query}]
            initial_response, _ = generate_response(query, tool_check_history, client, is_tool_check=True)

            tool_name, tool_result = tool_dispatcher(initial_response, client)
        
            if tool_name:
                conversation_history.append({"role": "user", "content": query})
                conversation_history.append({"role": "assistant", "content": f"Executed tool: {tool_name}"})
                save_history(conversation_history)
                listening = False
                return {
                    "success": True,
                    "response": f"Executed tool: {tool_name}",
                    "tool_result": tool_result
                }
            elif "[CHAT]" in initial_response:
                chat_response, conversation_history = generate_response(
                    _query=query,
                    history=conversation_history,
                    client=client
                )
                save_history(conversation_history)
                listening = False
                return {
                    "success": True,
                    "response": chat_response,
                }
            else:
                listening = False
                return {
                    "success": False,
                    "response": f"PulseAI (Fallback): {initial_response}",
                }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))