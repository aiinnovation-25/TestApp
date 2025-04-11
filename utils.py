# utils.py
import datetime
import random

class Logger:
    @staticmethod
    def log(message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

def greet(name: str) -> str:
    Logger.log(f"Greeting generated for {name}")
    return f"Hello, {name}!"

def generate_id() -> int:
    return random.randint(1000, 9999)
