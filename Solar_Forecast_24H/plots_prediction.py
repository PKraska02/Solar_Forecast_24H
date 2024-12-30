import os

import requests
from dotenv import load_dotenv

load_dotenv()

HA_URL = "http://your-home-assistant:8123"
HA_TOKEN = os.getenv("HA_TOKEN")
SENSOR_ENTITY_ID = "sensor.solarforecastAI"


def sent_data_to_plot(data):
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "state": data.mean(),  # Możesz ustawić średnią lub dowolną wartość jako stan główny
        "attributes": {
            "values": data.tolist()  # Przesyłanie NumPy array jako lista w atrybutach
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
