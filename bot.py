import requests
from dotenv import load_dotenv
import os
import pytz

import random
import schedule
import time
from datetime import datetime
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
                print("Bromita delivered :3")
                schedule.CancelJob
                return
        except Exception as error:
            print(f"\nError en attemp {attemp}: {error}")
            print(response.text)
        time.sleep(4)
    print("Bromita not succed :c")
    schedule.CancelJob


def schedule_tasks():

    # Defines the timezone for the reciever phone:
    local_timezone = pytz.timezone("America/Mexico_City")
    print("\nDaily schedule:", datetime.now().strftime("%d/%m/%Y"))

    # Schedule the morning bromita (Between 8:00am and 1:00pm):
    morning_hour = random.randint(8, 13)
    morning_minute = random.randint(0, 59)
    morning_time = local_timezone.localize(datetime(datetime.now().year, datetime.now().month, datetime.now().day, morning_hour, morning_minute))
    print(" - Morning bromita:", morning_time.strftime("%H:%M"))
    schedule.every().day.at(morning_time.strftime("%H:%M")).do(bromita)

    # Schedule the night bromita (Between 6:00pm and 11:00pm):
    night_hour = random.randint(18, 23)
    night_minute = random.randint(0, 59)
    night_time = local_timezone.localize(datetime(datetime.now().year, datetime.now().month, datetime.now().day, night_hour, night_minute))
    print(" - Night bromita:", night_time.strftime("%H:%M"))
    schedule.every().day.at(night_time.strftime("%H:%M")).do(bromita, night=True)


#? Main Point :3
if __name__ == "__main__":

    # Application running signal:
    print("Application running")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    # Defines the timezone for the reciever phone:
    local_timezone = pytz.timezone("America/Mexico_City")

    # Everyday at 6:00am it schedules a random hour to bromitas:
    scheduled_time = local_timezone.localize(datetime(datetime.now().year, datetime.now().month, datetime.now().day, 6, 0))
    schedule.every().day.at(scheduled_time.strftime("%H:%M")).do(schedule_tasks)

    # For eternity do:
    while True:
        schedule.run_pending()
        time.sleep(40)