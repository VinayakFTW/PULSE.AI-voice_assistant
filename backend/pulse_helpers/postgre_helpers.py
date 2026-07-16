import uuid
from datetime import datetime
from sqlalchemy.orm import Session

from backend.pulse_database.postgre_db import SessionLocal
from backend.pulse_models.database_model import Users, Sessions


def create_user(phone_number: str) -> int:
    db = SessionLocal()
    try:
        user = db.query(Users).filter(Users.phone_number == phone_number).first()
        if user:
            return user
        new_user = Users(phone_number=phone_number)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def get_user_by_phone(phone_number: str):
    db = SessionLocal()
    try:
        user = db.query(Users).filter(Users.phone_number == phone_number).first()
        return user
    finally:
        db.close()
    
def get_active_session_for_user(user_id: int):
    with SessionLocal() as db:
        record = (
            db.query(Sessions)
            .filter(Sessions.user_id == user_id)
            .order_by(Sessions.last_interaction_at.desc())
            .first()
        )
        return record.to_dict() if record else None

def create_active_session_for_user(user_id: str) -> str:
    """
    Creates a new active session for the given user in PostgreSQL and returns the session_id.
    """
    db = SessionLocal()
    new_session_id = str(uuid.uuid4())
    
    new_session = Sessions(
        session_id=new_session_id,
        user_id=user_id,
        last_interaction_at=datetime.utcnow(),
        created_at=datetime.utcnow()
    )
    
    try:
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        return new_session_id
    except Exception as e:
        db.rollback()
        print(f"Failed to create session for {user_id}: {str(e)}")
        raise e