import requests
from dotenv import load_dotenv
import os

from get_joke import get_joke

def bromita():
    #? Carga las variables de entorno:
    load_dotenv()
    API_ENDPOINT = os.getenv("API_ENDPOINT")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    TO_NUMBER = os.getenv("TO_NUMBER")

    #? Carga la bromita aleatoria:
    bromita_text = get_joke()
    bromita_text = " ".join(bromita_text.split())

    message = {
        "messaging_product": "whatsapp",
        "to": TO_NUMBER,
        "type": "template",
        "template": {
            "name": "bromita",
            "language": {"code": "es_MX"},
            "components": [
                {
                    "type": "BODY",
                    "parameters": [
                        {"type": "TEXT", "text": bromita_text}
                    ],
                }
            ],
        },
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_ENDPOINT, headers=headers, json=message)

    print(response.status_code)
    print(response.text)

bromita()