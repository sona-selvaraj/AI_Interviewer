from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base  # ✅ Correct import
import backend.models.interview as models


class UserInterview(Base):
    __tablename__ = "user_interviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    response_text = Column(String, nullable=False)
    chroma_id = Column(String, nullable=False)
