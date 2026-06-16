from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Absolute root imports that successfully loaded before
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse    
from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/api", tags=["Authentication"])


@router.post("/register", status_code=201)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """API endpoint to handle user signup."""
    # 1. Check if the email already exists in the database
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email already exists."
        )
    
    # 2. Hash the password safely
    hashed_pass = get_password_hash(user_in.password)    
    
    # 3. Create the database record blueprint using the model field
    new_user = User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=hashed_pass, 
        role=user_in.role
    )
    
    # 4. Commit the user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "message": "User registered successfully!",
        "name": new_user.name,
        "email": new_user.email,
        "role": new_user.role
    }


@router.post("/login")
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    """API endpoint to authenticate user and hand out a secure JWT Key."""
    # 1. Find user by email
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    
    # 2. Verify password matches the stored database hash field
    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    
    # 3. Package user role into token payload and sign it
    token_data = {"sub": user.email, "role": user.role, "name": user.name}
    access_token = create_access_token(data=token_data)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role
    }