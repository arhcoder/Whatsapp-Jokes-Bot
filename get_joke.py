import pandas as pd
import random

def get_joke():
    #/ To get a random joke from "bromitas.csv":
    try:
        bromitas = pd.read_csv("bromitas.csv")
        bromita = bromitas["text"][random.randint(0, bromitas.shape[0])]
        return bromita
    except:
        return "Hoy no hay bromita :c"
