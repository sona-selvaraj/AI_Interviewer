from fastapi import FastAPI
from backend.routes import auth, interview
from backend.database import Base, engine

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(interview.router, prefix="/interview", tags=["Interviews"])

@app.get("/")
def home():
    return {"message": "Welcome to AI Interviewer API!"}
