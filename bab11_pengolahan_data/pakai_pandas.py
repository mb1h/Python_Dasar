#  pandas 

from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).resolve().with_name("nilai.csv"))
print(df.groupby("kelas")["nilai"].mean())
print(df[df["nilai"] >= 75]["nama"].tolist())
print(df.sort_values("nilai").tail(1))
