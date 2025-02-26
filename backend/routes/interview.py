from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db, SessionLocal  # ✅ Import everything needed
from backend.models.interview import UserInterview
#from backend.chroma_setup import collection

# ✅ Define APIRouter
router = APIRouter()

@router.post("/store-response/")
async def store_response(user_id: int, response_text: str, db: Session = Depends(get_db)):
 #   chroma_id = f"user_{user_id}_response"
  #  collection.add(ids=[chroma_id], documents=[response_text], metadatas=[{"user_id": user_id}])

  #  db_response = UserInterview(user_id=user_id, response_text=response_text, chroma_id=chroma_id)
    db_response = UserInterview(user_id=user_id, response_text=response_text, chroma_id="dummy_id")
    db.add(db_response)
    db.commit()
    return {"message": "ChromaDB is disabled, search is unavailable"}


@router.get("/search-responses/")
async def search_responses(query: str):
    #results = collection.query(query_texts=[query], n_results=3)
    return {"message": "ChromaDB is disabled, search is unavailable"}

