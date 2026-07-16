from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.pulse_database.postgre_db import BASE

class Users(BASE):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, unique=True, index=True)
    verified = Column(Integer, default=0)  # 0 for not verified, 1 for verified
    created_at = Column(DateTime, default=datetime.utcnow)
    
    sessions = relationship("Sessions", back_populates="user", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLogs", back_populates="user", cascade="all, delete-orphan")


class Sessions(BASE):
    __tablename__ = "sessions"

    session_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    last_interaction_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("Users", back_populates="sessions")
    audit_logs = relationship("AuditLogs", back_populates="session", cascade="all, delete-orphan")



class AuditLogs(BASE):
    __tablename__ = "audit_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    session_id = Column(Integer, nullable=False)
    action = Column(String, nullable=False)
    response = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("Users", back_populates="audit_logs")
    session = relationship("Sessions", back_populates="audit_logs")