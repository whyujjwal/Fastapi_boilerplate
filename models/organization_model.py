from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    domain = Column(String(100), nullable=False)  # Example domain like "university.edu"
    
    # Relationship to access all professors in this organization
    professors = relationship('Professor', back_populates='organization')
