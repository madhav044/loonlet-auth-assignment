from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Absolute root imports
from app.database import get_db
from app.models.user import User
from app.core.security import get_current_user_from_token

router = APIRouter(prefix="/api", tags=["Protected Role Endpoints"])


@router.get("/admin/users")
def admin_only_route(current_user: dict = Depends(get_current_user_from_token), db: Session = Depends(get_db)):
    if current_user.get("role") != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Access denied: Admin permissions required."
        )
    users = db.query(User).all()
    return [{"name": u.name, "email": u.email, "role": u.role} for u in users]


@router.get("/therapist/dashboard")
def therapist_only_route(current_user: dict = Depends(get_current_user_from_token)):
    if current_user.get("role") != "Therapist":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Access denied: Therapist permissions required."
        )
    return {"message": f"Welcome, Therapist {current_user.get('name')}. Access granted to assigned parent data logs."}


@router.get("/parent/profile")
def parent_only_route(current_user: dict = Depends(get_current_user_from_token)):
    if current_user.get("role") != "Parent":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Access denied: Parent permissions required."
        )
    return {"message": f"Welcome, Parent {current_user.get('name')}. Profile verification data retrieved successfully."}