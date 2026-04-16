# Elective Project API

A simple starter API built with FastAPI.

## Setup

```bash
cd elective_project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## Endpoints

- `GET /` - status message
- `GET /health` - health check
- `POST /echo` - echoes the sent text

Example request body for `/echo`:

```json
{
  "text": "hello"
}
```
