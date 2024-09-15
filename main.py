from fastapi import FastAPI
from routers import user_router, admin_router
from utils.db import engine
from models import user_model




# Initialize the app
app = FastAPI()

app.include_router(user_router.router)
app.include_router(admin_router.router)

# Create the database tables
user_model.Base.metadata.create_all(bind=engine)
