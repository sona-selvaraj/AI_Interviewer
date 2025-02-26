from sqlalchemy import Column, Integer, String, Text
from backend.database import Base  # ✅ Correct import
import backend.models.user as models

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    experience = Column(Text, nullable=True)
    skills = Column(Text, nullable=True)
    interest_area = Column(Text, nullable=True)
