import requests

def get_session_token(api_key: str, request_token: str, checksum: str) -> dict:
    """
    Sends a POST request to Kite API to generate a session token.

    Args:
        api_key (str): Your Kite API key
        request_token (str): The request token received after login
        checksum (str): SHA256 checksum (api_key + request_token + api_secret)

    Returns:
        dict: JSON response from the API
    """
    url = "https://api.kite.trade/session/token"
    headers = {
        "X-Kite-Version": "3",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "api_key": api_key,
        "request_token": request_token,
        "checksum": checksum
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status() 
    print(response.json()["data"]["access_token"])
    return response.json()["data"]["access_token"]