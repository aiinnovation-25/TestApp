# service.py
from utils import greet

def process_request(name: str) -> str:
    return greet(name)
