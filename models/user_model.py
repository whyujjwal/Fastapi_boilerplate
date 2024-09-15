from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from .base_class import Base
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), index=True, nullable = False)
    email = Column(String(120), unique=True, index=True)
    hashed_password = Column(String)
    profile_info = Column(String, nullable = True)
    role = Column(String, default="user")  # "admin" or "user" or "prof" or "student" or "ta"
    phone_number = Column(String, unique=True) #change into int for future use 
    is_verified = Column(Boolean, default = False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    



# ID - PK
# Name 
# Email ID
# Hashed Password
# Profile Info 
# Phone Number -
# Verification
# TA / Prof / Student  
