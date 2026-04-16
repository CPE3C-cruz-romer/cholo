from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Elective Project API", version="1.0.0")


class MessageResponse(BaseModel):
    message: str


class EchoRequest(BaseModel):
    text: str


@app.get("/", response_model=MessageResponse)
def root() -> MessageResponse:
    return MessageResponse(message="Elective Project API is running")


@app.get("/health", response_model=MessageResponse)
def health() -> MessageResponse:
    return MessageResponse(message="ok")


@app.post("/echo", response_model=MessageResponse)
def echo(payload: EchoRequest) -> MessageResponse:
    return MessageResponse(message=payload.text)
