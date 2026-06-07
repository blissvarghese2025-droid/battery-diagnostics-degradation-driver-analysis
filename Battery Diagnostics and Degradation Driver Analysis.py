import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


battery_data = pd.read_csv("new_battery_charging.csv")
print(battery_data.columns)

print(battery_data.info())

print("\nMissing Values")
print(battery_data.isnull().sum())

print("\nDuplicate Rows")
print(battery_data.duplicated().sum())

print("\nStatistics")
print(battery_data.describe())

plt.figure(figsize=(8,5))
plt.hist(battery_data['SOH'], bins=30)
plt.title("SOH Distribution")
plt.xlabel("SOH")
plt.ylabel("Count")
plt.savefig("SOH_distribution.png")
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(
    battery_data['battery_temp'],
    battery_data['SOH']
)

plt.xlabel("Battery Temperature")
plt.ylabel("SOH")
plt.title("SOH vs Temperature")
plt.savefig("SOH_vs_Temperature.png")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(
    battery_data['internal_resistance'],
    battery_data['SOH']
)

plt.xlabel("Internal Resistance")
plt.ylabel("SOH")
plt.title("SOH vs Internal Resistance")
plt.savefig("SOH_vs_Internal Resistance.png")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(
    battery_data['charging_efficiency'],
    battery_data['SOH']
)

plt.xlabel("Charging efficiency")
plt.ylabel("SOH")
plt.title("SOH vs Charging efficiency")
plt.savefig("SOH_vs_Charging_efficiency.png")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(
    battery_data['thermal_stress_index'],
    battery_data['SOH']
)

plt.xlabel("Thermal Stress Index")
plt.ylabel("SOH")
plt.title("SOH vs Thermal Stress")
plt.savefig("SOH_vs_Thermal_Stress.png")
plt.show()



selected_columns = [
    'SOH',
    'battery_temp',
    'internal_resistance',
    'thermal_stress_index',
    'aging_indicator',
    'charging_efficiency',
    'cycle_degradation'
]

corr_matrix = battery_data[selected_columns].corr()

print(corr_matrix)

correlation_to_soh = corr_matrix['SOH']

print(
    correlation_to_soh.sort_values()
)

print("\nTop Degradation Drivers:")

print(
    correlation_to_soh
    .drop('SOH')
    .sort_values()
    .head(3)
)

plt.figure(figsize=(8,6))
plt.imshow(corr_matrix, cmap='coolwarm')
plt.colorbar()

plt.xticks(
    range(len(corr_matrix.columns)),
    corr_matrix.columns,
    rotation=45
)

plt.yticks(
    range(len(corr_matrix.columns)),
    corr_matrix.columns
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("correlation_matrix.png")

plt.show()

def battery_status(soh):

    if soh >= 90:
        return "Healthy"
    
    elif soh >= 80:
        return "Monitor"
    
    else:
        return "Inspect"
    

battery_data['Status'] = battery_data['SOH'].apply(battery_status)

print(
    battery_data['Status'].value_counts()
)

average_SOH = battery_data['SOH'].mean()

print("\nFleet Health Summary")
print("-------------------")
print(f"Average SOH: {average_SOH:.2f}")

print(
    battery_data.groupby('Status')['SOH']
    .mean()
)











