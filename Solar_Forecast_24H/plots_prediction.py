import os

import requests
from dotenv import load_dotenv

load_dotenv()

HA_URL = "http://192.168.202.115:8124/"
HA_TOKEN = os.getenv("HA_TOKEN")
SENSOR_ENTITY_ID = "sensor.solarforecastAI"


def sent_data_to_plot(data):
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "state": "On",  # Konwersja na standardowy float
        "attributes": {
            "values": [float(x) for x in data]  # Konwersja wszystkich wartości na float
        }
    }

    response = requests.post(
        f"{HA_URL}/api/states/{SENSOR_ENTITY_ID}",
        json=payload,
        headers=headers,
    )
    if response.status_code == 200:
        print(f"Data sent successfully! Response: {response.json()}")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
        print(f"Error: {response.text}")

