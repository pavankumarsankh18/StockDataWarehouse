import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


from kite_historical_api.kite_fetch_historical_data import fetch_historical_data
from session_setup import load_api_credentials

filepath = "kite_instruments/instruments.json"

def get_instruments_to_process():
    with open(filepath, "r") as f:
        instruments = json.load(f)
    return instruments


def get_datetime_range(ticker) -> str:
    """
    Return the current local datetime formatted as 'YYYY-MM-DD+HH:MM:SS'.
    """
    past = ticker - relativedelta(days=60)
    return {
        "from_time" : past.strftime("%Y-%m-%d"), #+ "+09:15:00",
        "to_time" : ticker.strftime("%Y-%m-%d") #+ "+15:15:00"
        }

def main():
    instruments = get_instruments_to_process()
    creds = load_api_credentials("secrets/kite_secretes.json")
    now = datetime.now()
    range = get_datetime_range(now)
    for instrument in instruments:
        print(f"Fetching for stock: {instrument} and Kite-instrument ID: {instruments[instrument]}")
        response = fetch_historical_data(
            instrument_token=instruments[instrument],
            from_time=range['from_time'],
            to_time=range['to_time'],
            api_key=creds["api_key"],
            access_token=creds["access_token"]
        )
        print(response)


if __name__ == "__main__":
    main()