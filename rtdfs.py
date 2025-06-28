import requests
import time
import random
from datetime import datetime

URL = "http://(((url)))/sendData" 

def generate_data_unit():
    return {
        "ID": "sensor-1",
        "sID": random.randint(0, 10),
        "dt": datetime.now().isoformat(),
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
