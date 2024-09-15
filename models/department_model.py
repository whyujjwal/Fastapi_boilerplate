from .base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, ForeignKey

class Department(Base):
    
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    professors = relationship('Professor', back_populates='department') #to list all the professors in a department
    hod_id = Column(Integer, ForeignKey('professors.id'), nullable = True) #for the time being nullable is set to true
    