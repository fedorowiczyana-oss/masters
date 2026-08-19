from pathlib import Path
import pandas as pd
import re

DATA_ROOT = Path("data/alfa/processed/processed")  # у тебя так и есть

def extract_label(folder_name: str) -> str:
    name = folder_name.lower()
    if "no_failure" in name:
        return "NORMAL"
    if "engine_failure" in name:
        return "ENGINE"
    if "aileron" in name:
        return "AILERON"
    if "rudder" in name:
        return "RUDDER"
    return "UNKNOWN"

rows = []

for flight_dir in sorted(DATA_ROOT.iterdir()):
    if not flight_dir.is_dir():
        continue

    label = extract_label(flight_dir.name)
    if label == "UNKNOWN":
        continue  # пропускаем no_ground_truth и странные кейсы

    csv_files = list(flight_dir.glob("*.csv"))
    rows.append({
        "flight_id": flight_dir.name,
        "label": label,
        "n_csv": len(csv_files),
        "path": str(flight_dir),
    })

df_flights = pd.DataFrame(rows)
df_flights.head(), df_flights["label"].value_counts()
