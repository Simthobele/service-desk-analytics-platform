from fastapi import FastAPI

app = FastAPI(
    title="Service Desk Analytics Platform",
    description="Analytics platform for Service Desk performance monitoring.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "running",
        "application": "Service Desk Analytics Platform",
        "version": "1.0.0"
    }