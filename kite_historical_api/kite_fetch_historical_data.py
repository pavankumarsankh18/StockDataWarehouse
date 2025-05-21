import requests

def fetch_historical_data(
    instrument_token: str,
    from_time: str,
    to_time: str,
    api_key: str,
    access_token: str,
    interval: str = "day"
) -> dict:
    """
    Fetch historical data from Kite API.

    Args:
        instrument_token (str): The instrument token (e.g., "5633")
        from_time (str): Start time in ISO format (e.g., "2017-12-15 09:15:00")
        to_time (str): End time in ISO format (e.g., "2017-12-15 09:20:00")
        api_key (str): Your Kite API key
        access_token (str): Your Kite access token
        interval (str): Interval for data (default: "minute")

    Returns:
        dict: JSON response from the Kite API
    """
    base_url = "https://api.kite.trade/instruments/historical"
    endpoint = f"{base_url}/{instrument_token}/{interval}"
    params = {
        "from": from_time,
        "to": to_time
    }
    headers = {
        "X-Kite-Version": "3",
        "Authorization": f"token {api_key}:{access_token}"
    }

    response = requests.get(endpoint, headers=headers, params=params)
    print(response)
    response.raise_for_status()  # Raise error for HTTP issues
    return response.json()
