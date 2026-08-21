import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Q01_solar_farm.csv")

print(df.head())
print(df.info())
print(df.describe())

print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df = df.dropna()

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["Hour"] = df["timestamp"].dt.hour

print("\nDescriptive Stats:")
print(df[["panel_output_kwh", "ambient_temperature_c", "sunlight_duration_hours"]].describe())

df["Generation_Efficiency"] = df["panel_output_kwh"] / df["sunlight_duration_hours"]

def classify_time(hour):
    if hour < 12:
        return "Morning"
    elif hour < 17:
        return "Afternoon"
    else:
        return "Evening"
    

df["Time_of_Day"] = df["Hour"].apply(classify_time)

print("\nEfficiency Stats:")
print(df[["panel_output_kwh", "ambient_temperature_c", "sunlight_duration_hours", "Generation_Efficiency"]].describe())

df.to_csv("cleaned_solar_farm.csv", index=False)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="ambient_temperature_c", y="panel_output_kwh", hue="Time_of_Day")
plt.xlabel("Ambient Temperature (°C)")
plt.ylabel("Panel Output (kWh)")
plt.title("Temperature vs Solar Panel Output")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
df_sorted = df.sort_values("sunlight_duration_hours")
plt.plot(df_sorted["sunlight_duration_hours"], df_sorted["panel_output_kwh"], marker="o", linewidth=1)
plt.xlabel("Sunlight Duration (hours)")
plt.ylabel("Panel Output (kWh)")
plt.title("Sunlight Duration vs Panel Output")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Time_of_Day", y="Generation_Efficiency", order=["Morning", "Afternoon", "Evening"])
plt.xlabel("Time of Day")
plt.ylabel("Generation Efficiency (kWh/hr)")
plt.title("Generation Efficiency by Time of Day")
plt.tight_layout()
plt.show()

print("\nCorrelation with Generation_Efficiency:")
print(df[["panel_output_kwh", "ambient_temperature_c", "sunlight_duration_hours",
          "panel_capacity_kw", "Generation_Efficiency"]].corr()["Generation_Efficiency"].drop("Generation_Efficiency"))
