import requests
from config import API_KEY

def get(endpoint, params=None, headers=None):
    headers = headers or {}
    headers["Authorization"] = f"Bearer {API_KEY}"
    response = requests.get(endpoint, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def post(endpoint, data=None, headers=None):
    headers = headers or {}
    headers["Authorization"] = f"Bearer {API_KEY}"
    headers["Content-Type"] = "application/json"
    response = requests.post(endpoint, json=data, headers=headers)
    response.raise_for_status()
    return response.json()
