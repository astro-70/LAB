import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Q01_solar_farm.csv")
df = df.drop_duplicates()
df = df.dropna()

print(df.columns.tolist())

df["Generation_Efficiency"] = df["panel_output_kwh"] / df["sunlight_duration_hours"]

plt.figure(figsize=(8, 5))
plt.scatter(df["ambient_temperature_c"], df["panel_output_kwh"], color="steelblue", edgecolors="white", alpha=0.8)
plt.title("Temperature vs Daily Solar Generation")
plt.xlabel("Ambient Temperature (°C)")
plt.ylabel("Panel Output (kWh)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

plt.figure(figsize=(8, 5))
df_sorted = df.sort_values("sunlight_duration_hours")
sns.lineplot(data=df_sorted, x="sunlight_duration_hours", y="panel_output_kwh", color="darkorange")
plt.title("Sunlight Duration vs Daily Solar Generation")
plt.xlabel("Sunlight Duration (hours)")
plt.ylabel("Panel Output (kWh)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()
