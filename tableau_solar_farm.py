import pandas as pd

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

df.to_csv("tableau_solar_farm.csv", index=False)
print("tableau_solar_farm.csv created successfully.")
