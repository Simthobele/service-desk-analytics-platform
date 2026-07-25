from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine

app = FastAPI(
    title="Service Desk Analytics Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "Service Desk Analytics Platform",
        "status": "running"
    }


@app.get("/health/database")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "Connected"
        }

    except Exception as error:
        return {
            "database": "Failed",
            "error": str(error)
        }