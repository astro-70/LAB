import pandas as pd
import os
import shutil

df = pd.read_csv("Q01_solar_farm.csv")
df = df.drop_duplicates()
df = df.dropna()

df["Generation_Efficiency"] = df["panel_output_kwh"] / df["sunlight_duration_hours"]
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["Hour"] = df["timestamp"].dt.hour
df["Date"] = df["timestamp"].dt.date

def classify_time(hour):
    if hour < 12:
        return "Morning"
    elif hour < 17:
        return "Afternoon"
    else:
        return "Evening"

df["Time_of_Day"] = df["Hour"].apply(classify_time)

# Save to project folder
project_csv = "tableau_solar_farm.csv"
df.to_csv(project_csv, index=False)
print(f"Saved: {project_csv}")

# Save to Tableau temp path
tableau_temp = r"C:/Users/astro/AppData/Local/Temp/TableauTemp/113rw090jr5rgg1ee04d41p9npy2"
tableau_csv = os.path.join(tableau_temp, "Q01_solar_farm_cleaned.csv.csv")

os.makedirs(tableau_temp, exist_ok=True)
shutil.copy(project_csv, tableau_csv)
print(f"Saved to Tableau temp: {tableau_csv}")
