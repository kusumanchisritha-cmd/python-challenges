import random
import math
import numpy as np
import pandas as pd
data = []

choice = input("Enter mode (1: Manual, 2: Random): ")
n = int(input("Enter number of zones: "))

for i in range(1, n+1):
    if choice == "1":
        print(f"\nZone {i}")
        traffic = int(input("Traffic (0-100): "))
        air = int(input("Air Quality (0-300): "))
        energy = int(input("Energy (0-500): "))
    else:
        traffic = random.randint(0, 100)
        air = random.randint(0, 300)
        energy = random.randint(0, 500)

    data.append({
        "zone": i,
        "traffic": traffic,
        "air_quality": air,
        "energy": energy
    })
def classify(d):
    if d["air_quality"] > 200 or d["traffic"] > 80:
        return "High Risk"
    elif d["energy"] > 400:
        return "Energy Critical"
    elif d["traffic"] < 30 and d["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def risk(d):
    return d["traffic"]*0.5 + d["air_quality"]*0.3 + d["energy"]*0.2
def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]["risk_score"] < arr[j+1]["risk_score"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def decision(avg):
    if avg < 80:
        return "City Stable"
    elif avg < 120:
        return "Moderate Risk"
    elif avg < 180:
        return "High Alert"
    else:
        return "Critical Emergency"
for d in data:
    d["category"] = classify(d)
    d["risk_score"] = risk(d)
    d["sqrt"] = math.sqrt(d["risk_score"])
roll_no = 10

if roll_no % 3 == 0:
    random.shuffle(data)
else:
    data = custom_sort(data)
df = pd.DataFrame(data)
top3 = data[:3]
max_r = max(df["risk_score"])
min_r = min(df["risk_score"])
avg_r = sum(df["risk_score"]) / len(df)
risk_tuple = (max_r, avg_r, min_r)
final = decision(avg_r)
print("\nDataFrame:")
print(df)
print("\nCategorized Zones:")
print(df[["zone", "category"]])
print("\nTop Risk Zones:")
for t in top3:
    print("Zone", t["zone"], "->", t["risk_score"])
print("\nRisk Tuple:")
print(risk_tuple)
print("\nFinal Decision:")
print(final)
print("\nInsight:")
print("A smart city maintains balance in traffic, pollution, and energy usage.")