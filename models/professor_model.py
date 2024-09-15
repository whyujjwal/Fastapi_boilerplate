import user_model
from sqlalchemy.orm import  relationship
from sqlalchemy import Integer, String, Column, ForeignKey

class Professor(user_model.User):
    __tablename__ = 'professors'
    
    
    id = Column(Integer, primary_key=True, autoincrement=True)  
    department = Column(String(100), nullable=False)
    office_number = Column(String(50), nullable=True)
    
    #organization relationship
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    organization_sso = Column(String(150), nullable=False) 
    
    
    # Relationship to link Professor to Organization
    organization = relationship('Organization', back_populates='professors')
    department = relationship('Department', back_populates='professors')