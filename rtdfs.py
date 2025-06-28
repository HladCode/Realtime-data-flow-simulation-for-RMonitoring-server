import requests
import time
import random
from datetime import datetime, timezone, timedelta

URL = "http://(((url)))/sendData" 

def generate_data_unit():
    utc_plus_3 = timezone(timedelta(hours=3))
    return {
        "ID": "Data-flow-simulation-1",
        "sID": 0,
        "dt": datetime.now(utc_plus_3).isoformat(),
        "d": random.uniform(-10, 10)
    }


while True:
    payload = {
        "AllCurrentData": [generate_data_unit()]
    }

    try:
        response = requests.post(URL, json=payload)
        print(f"[{datetime.now().isoformat()}] Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error sending data: {e}")

    time.sleep(5)
