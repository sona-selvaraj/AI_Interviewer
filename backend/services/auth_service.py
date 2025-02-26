from passlib.context import CryptContext
import os
from jose import jwt
import os
from datetime import datetime, timedelta

# Manually load .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            key, value = line.strip().split("=", 1)
            os.environ[key] = value


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(data: dict, expires_delta: timedelta = timedelta(hours=2)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

