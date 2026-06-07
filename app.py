import requests

def get_user(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

def calculate_total(items):
    # Bug: crashes on empty list
    return sum(items) / len(items)