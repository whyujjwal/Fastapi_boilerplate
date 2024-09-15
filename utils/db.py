from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgres://avnadmin:AVNS_sSwPwLTEupO0arewyvZ@pg-1eaecb39-smartqna-be.c.aivencloud.com:18312/pg-1eaecb39-smartqna-be.c.aivencloud.com" #put in env variable later on
DATABASE_URL = "sqlite:///./smartqna.db" 

# engine = create_engine(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
