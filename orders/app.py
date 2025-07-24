# orders/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Orders service!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
