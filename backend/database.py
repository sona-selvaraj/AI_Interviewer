from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Manually load .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            key, value = line.strip().split("=", 1)
            os.environ[key] = value

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL is not set! Check your .env file and environment variables.")

# Initialize database connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency function for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
