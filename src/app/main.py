from fastapi import Depends, FastAPI, HTTPException, Request, Response
from typing import List
from sqlalchemy.orm import Session
from app.api import crud, models, schemas
from app.database import SessionLocal, engine
from redis import Redis

# Uncomment the line below to let the ORM generate tables and relationships for us - if not using migrations
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# DB Dependency
def get_db(request: Request):
    return request.state.db

# health checker
@app.get("/health")
async def root():
    return {"message": "I am healthy"}

# Basic crud operations
# @app.post("/appointment/", response_model=schemas.Brewer)

# @app.get("/appointments", response_model=List[schemas.Brewer])

# @app.get("/appointment/{id}", response_model=schemas.Recipe)

# @app.delete("/appointment/{id}", status_code=200)

# @app.put("/appointment/{id}", response_model=schemas.Brewer)
