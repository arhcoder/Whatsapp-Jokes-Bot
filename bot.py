import requests
from dotenv import load_dotenv
import os

import random
import schedule
import time
from datetime import datetime, timedelta
from get_joke import get_joke


def bromita(night: bool = False):
    #? Carga las variables de entorno:
    load_dotenv()
    API_ENDPOINT = os.getenv("API_ENDPOINT")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    TO_NUMBER = os.getenv("TO_NUMBER")

    #? Carga la bromita aleatoria:
    bromita_text = get_joke()
    bromita_text = " ".join(bromita_text.split())

    joke_time = "bromita_noche" if night else "bromita"
    message = {
        "messaging_product": "whatsapp",
        "to": TO_NUMBER,
        "type": "template",
        "template": {
            "name": joke_time,
            "language": {"code": "es_MX"},
            "components": [
                {
                    "type": "BODY",
                    "parameters": [
                        {"type": "TEXT", "text": bromita_text}
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Try to get a bromita:
    max_attempts = 3
    for attemp in range(1, max_attempts + 1):
        try:
            response = requests.post(API_ENDPOINT, headers=headers, json=message)
            if response.status_code == 200:
                print("ok")
                return
        except Exception as error:
            print(f"\nError en attemp {attemp}: {error}")
            print(response.text)
        time.sleep(4)
    print("Bromita not succed :c")


def schedule_tasks():

    # Schedule the morning bromita (Between 8:00am and 1:00pm):
    morning_hour = random.randint(8, 12)
    morning_minute = random.randint(0, 59)
    morning_time = f"{morning_hour:02d}:{morning_minute:02d}"
    print(morning_time)
    schedule.every().day.at(morning_time).do(bromita)

    # Schedule the night bromita (Between 6:00pm and 11:00pm):
    night_hour = random.randint(18, 22)
    night_minute = random.randint(0, 59)
    night_time = f"{night_hour:02d}:{night_minute:02d}"
    print(night_time)
    schedule.every().day.at(night_time).do(bromita, night=True)


#? Main Point :3
if __name__ == "__main__":

    # Everyday at 00:00am it schedules a random hour to bromitas:
    schedule.every().day.at("00:00").do(schedule_tasks)

    # For eternity do:
    while True:
        schedule.run_pending()
        time.sleep(40)