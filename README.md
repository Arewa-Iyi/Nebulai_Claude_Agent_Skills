# Nebulai AgentSkills Example

A minimal FastAPI project scaffold inspired by the repository layout shown in the screenshot.

## Features

- FastAPI application structure
- Database configuration with SQLAlchemy
- User authentication with JWT
- Example routers for auth, users, tasks, payments, transactions
- Pydantic schemas and SQLAlchemy models

## Run locally

1. Create and activate a Python environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the app:

```powershell
uvicorn main:app --reload
```

4. Open `http://127.0.0.1:8000/docs`
