from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Message(BaseModel):
    name: str
    message: str

@app.get("/")
def read_root():
    return {
        "status": "Application Running",
        "timestamp": datetime.now()
    }

@app.post("/send")
def send_message(data: Message):
    return {
        "received_from": data.name,
        "message": data.message,
        "processed_at": datetime.now()
    }
#testing automatic PR