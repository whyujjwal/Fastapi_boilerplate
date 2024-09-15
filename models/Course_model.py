from .base_class import Base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    organization_id = Column(Integer, ForeignKey('departments.id'))
    credits = Column(Integer, nullable=False, default=0)
    
    # Courses many-to-many relationship don't need this for the time being 
    # courses = relationship('Course', secondary=professor_courses, back_populates='professors') 