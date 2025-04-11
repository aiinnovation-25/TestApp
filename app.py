# app.py
from fastapi import FastAPI
from service import process_request, UserService

app = FastAPI()
user_service = UserService()

@app.get("/greet/{name}")
def greet_user(name: str):
    return process_request(name)

@app.post("/user/{name}")
def create_user(name: str):
    return user_service.create_user(name)

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return user_service.get_user(user_id)

