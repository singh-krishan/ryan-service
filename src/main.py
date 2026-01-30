"""
A Python microservice
"""
from fastapi import FastAPI
import os

app = FastAPI(
    title="ryan-service",
    description="A Python microservice",
    version="0.1.0"
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to ryan-service",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "ryan-service"
    }


@app.get("/hello")
async def hello():
    """Custom hello endpoint."""
    return {
        "message": "hello, welcome to my IDP"
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8005"))
    uvicorn.run(app, host="0.0.0.0", port=port)
