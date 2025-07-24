# auth/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Auth service!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
