from fastapi import FastAPI
from routers import user_router
from routers import user_router
from utils.db import engine
from models import user_model


# Initialize the app
app = FastAPI()

# Include the user router
app.include_router(user_router.router)

# Create the database tables
user_model.Base.metadata.create_all(bind=engine)
