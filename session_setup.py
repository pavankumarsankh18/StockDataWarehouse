from hashlib import sha256
import json
from kite_historical_api.kite_session import get_session_token


def generate_checksum(api_key: str, request_token: str, api_secret: str) -> str:
    """
    Generate SHA256 checksum from api_key, request_token, and api_secret.
    """
    input_string = api_key + request_token + api_secret
    return sha256(input_string.encode('utf-8')).hexdigest()

def load_api_credentials(filepath: str = "secrets.json") -> dict:
    """
    Load API credentials from a JSON file.

    Args:
        filepath (str): Path to the JSON file (default: secrets.json)

    Returns:
        dict: Dictionary with keys 'api_key', 'request_token', and 'api_secret'
    """
    with open(filepath, "r") as f:
        credentials = json.load(f)

    required_keys = {"api_key", "request_token", "api_secret"}
    if not required_keys.issubset(credentials.keys()):
        raise ValueError(f"Missing one or more required keys in {filepath}")

    return credentials

import json
import os

def update_access_token(access_token: str, filepath: str = "secrets.json") -> None:
    """
    Update or create the 'access_token' entry in the secrets.json file.

    Args:
        access_token (str): The new access token to store.
        filepath (str): Path to the secrets JSON file (default: secrets.json).
    """
    secrets = {}

    # Load existing secrets if file exists
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try:
                secrets = json.load(f)
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON format in {filepath}")

    # Update or insert access_token
    secrets["access_token"] = access_token

    # Save back to the file
    with open(filepath, "w") as f:
        json.dump(secrets, f, indent=4)
    print(f"✅ Access token updated in {filepath}")


def main():
    filepath = "secrets/kite_secretes.json"
    credentials = load_api_credentials(filepath)
    api_key = credentials["api_key"]
    request_token = credentials["request_token"]
    api_secret = credentials["api_secret"]

    checksum = generate_checksum(api_key, request_token, api_secret)
    print("✅ Generated Checksum:", checksum)

    access_token = get_session_token(api_key=api_key, request_token=request_token, checksum=checksum)
    print("✅ Generated access_token:", access_token)

    update_access_token(access_token=access_token, filepath=filepath)

if __name__ == "__main__":
    main()
