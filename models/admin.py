from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import user_model

class Admin(user_model.User):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
