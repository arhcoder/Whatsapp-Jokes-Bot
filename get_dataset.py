from datasets import load_dataset
import pandas as pd

dataset = load_dataset("mrm8488/CHISTES_spanish_jokes")
df = pd.DataFrame(dataset["train"])
df.to_csv("bromitas.csv", index=False)