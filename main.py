from fastapi import FastAPI
from app.routers import auth, users, tasks, payments, transactions
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nebulai AgentSkills")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
