from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schema import user_schema
from models import user_model
from .user_router import get_current_user


router = APIRouter()

# Admin-only dependency
def get_current_admin(current_user: user_model.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return current_user


# Admin-only route
@router.get("/admin", response_model=user_schema.UserResponse)
def read_admin_data(current_admin: user_model.User = Depends(get_current_admin)):
    return current_admin
