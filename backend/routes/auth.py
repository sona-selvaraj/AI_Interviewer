from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.user import User
from backend.services.auth_service import hash_password, verify_password, create_jwt_token
from pydantic import BaseModel

router = APIRouter()

class SignupModel(BaseModel):
    username: str
    email: str
    password: str
    experience: str
    skills: str
    interest_area: str

class LoginModel(BaseModel):
    email: str
    password: str

@router.post("/signup/")
def signup(user: SignupModel, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        experience=user.experience,
        skills=user.skills,
        interest_area=user.interest_area
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/login/")
def login(user: LoginModel, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user or not verify_password(user.password, existing_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_jwt_token({"email": user.email, "username": existing_user.username})
    return {"token": token}
