import os
import httpx
import vobject
from rapidfuzz import process, fuzz

from pulse_ear.speech_handler import speak
from backend.pulse_controllers.openwa_controllers.get_wa_session import get_wa_session_id
from backend.pulse_controllers.openwa_controllers.get_wa_session_chats import get_wa_session_chats

OPENWA_URL = os.getenv("OPENWA_URL")
OPENWA_API_KEY = os.getenv("OPENWA_API_KEY")

def get_vcf_contacts(file_path):
    """
    Parses a .vcf file and returns a dictionary of contacts.
    """
    contacts = {}
    try:
        with open(file_path, 'r') as f:
            for card in vobject.readComponents(f):
                if hasattr(card, 'fn'):
                    name = card.fn.value
                    phone = None
                    if hasattr(card, 'tel'):
                        phone = card.tel.value
                    contacts[name.lower()] = {
                        'name': name,
                        'phone': phone,
                        'email': None
                    }
        return contacts
    except Exception as e:
        print(f"Error parsing VCF file: {e}")
        return {}
    
def get_best_contact_match(input_name: str, vcf_path: str) -> tuple[str, str] | None:
    """
    Finds the closest matching contact name using fuzzy logic.
    Returns (matched_name, phone_number) if a strong match is found.
    """
    names = list(get_vcf_contacts(vcf_path).keys())
    
    result = process.extractOne(input_name, names, scorer=fuzz.token_sort_ratio)
    
    if result:
        matched_name, score, _ = result
        if score >= 80:
            return matched_name, get_vcf_contacts(vcf_path)[matched_name]['phone']
            
    return None

def find_contact(name):
    current_dir = os.path.dirname(__file__) 
    vcf_path = os.path.join(current_dir, '..', 'contacts.vcf')
    best_match = get_best_contact_match(name, vcf_path)
    if best_match:
        return {'name': best_match[0], 'phone': best_match[1]}
    return None

def send_whatsapp_message(contact_name, message):
    if not contact_name or not message:
        speak("I'm missing some information. Who should I message and what should it say?")
        return

    contact = find_contact(contact_name)
    if contact and contact['phone']:
        full_message = f"{message}\n**Sent by Pulse AI**"
        try:
            session_id = get_wa_session_id()
            session_chats = get_wa_session_chats(session_id=session_id)
            chat_id = None
            for _ in session_chats:
                if session_chats['contact'] == contact['phone']:
                    chat_id = session_chats['chat_id']
                    break
            url = f"{OPENWA_URL}/api/sessions/{session_id}/messages/send-text"
            payload = {
                "chatId": chat_id,
                "text": full_message, 
            }
            
            headers = {
                "X-API-Key": OPENWA_API_KEY,
            }
            try:
                request = httpx.post(url, json=payload, headers=headers)
                request.raise_for_status()
            except httpx.HTTPError as e:
                print(f"Error sending WhatsApp message: {e}")
                speak("Sorry, I couldn't send the message.")
                return False
            speak("Message sent successfully!")
            return True
        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")
            speak("Sorry, I couldn't send the message.")
            return False
    else:
        speak(f"Sorry, I couldn't find {contact_name} in your contacts.")
        return False