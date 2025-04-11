# service.py
from utils import greet, generate_id, Logger

class UserService:
    def __init__(self):
        self.users = {}
    
    def create_user(self, name: str) -> dict:
        user_id = generate_id()
        self.users[user_id] = name
        Logger.log(f"User created: {name} with ID {user_id}")
        return {"id": user_id, "name": name}

    def get_user(self, user_id: int) -> dict:
        name = self.users.get(user_id, "Unknown")
        Logger.log(f"User fetched: {user_id} -> {name}")
        return {"id": user_id, "name": name}

def process_request(name: str) -> dict:
    user_service = UserService()
    user = user_service.create_user(name)
    return {"message": greet(user["name"]), "user": user}
