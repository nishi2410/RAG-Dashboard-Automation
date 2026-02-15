from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
# Import your schemas and DB config here

app = FastAPI(title="RAG Dashboard API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the RAG Dashboard Automation API"}