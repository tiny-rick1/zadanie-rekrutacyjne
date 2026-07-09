import os

from fastapi import FastAPI

app = FastAPI(title="DevOps Recruitment Task")


@app.get("/health-check")
def health_check():
    return {"status": "ok"}


@app.get("/hello-world")
def hello_world():
    return os.environ.get("SERVER_HELLO", "Hello, World!")
