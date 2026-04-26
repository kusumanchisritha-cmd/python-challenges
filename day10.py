import math
import copy
import numpy as np
import pandas as pd

def get_user_input():
    zones = int(input("Enter number of zones: "))
    roll = int(input("Enter your roll number: "))
    return zones, roll

def generate_zone(zone_id):
    print(f"\nEnter data for Zone {zone_id}")

    traffic = int(input("Traffic: "))
    pollution = int(input("Pollution: "))
    energy = int(input("Energy: "))

    history = list(map(int, input("Enter 5 history values: ").split()))

    return {
        "zone": zone_id,
        "metrics": {
            "traffic": traffic,
            "pollution": pollution,
            "energy": energy
        },
        "history": history
    }


def generate_data(n):
    return [generate_zone(i) for i in range(1, n+1)]

def personalize_data(data, roll):
    if roll % 2 == 0:
        return list(reversed(data))
    else:
        return data[3:] + data[:3]

def create_copies(data):
    return data, copy.copy(data), copy.deepcopy(data)

def mutate_data(data):
    for item in data:
        item["metrics"]["traffic"] += 5
        item["metrics"]["pollution"] -= 2
        item["metrics"]["energy"] += 3
        item["history"].append(50)

def risk_score(metrics):
    return math.log(metrics["traffic"] + metrics["pollution"] + metrics["energy"])

def to_dataframe(data):
    rows = []
    for item in data:
        m = item["metrics"]
        rows.append({
            "zone": item["zone"],
            "traffic": m["traffic"],
            "pollution": m["pollution"],
            "energy": m["energy"],
            "risk": risk_score(m)
        })
    return pd.DataFrame(rows)

def analyze(df):
    arr = df[["traffic", "pollution", "energy", "risk"]].values

    mean = np.mean(arr, axis=0)
    variance = np.var(arr, axis=0)

    x = arr[:, 0]
    y = arr[:, 1]

    if len(x) < 3:
        corr = 0
    else:
        numerator = np.sum((x - np.mean(x)) * (y - np.mean(y)))
        denominator = (
            np.sqrt(np.sum((x - np.mean(x))**2)) *
            np.sqrt(np.sum((y - np.mean(y))**2))
        )

        if denominator == 0:
            corr = 0
        else:
            corr = numerator / denominator

    return mean, variance, corr

def detect_anomalies(df):
    mean = df["risk"].mean()
    std = df["risk"].std()
    return df[df["risk"] > mean + std]

def detect_clusters(df):
    risky = df["risk"] > df["risk"].mean()
    clusters, temp = [], []

    for i, val in enumerate(risky):
        if val:
            temp.append(df.iloc[i]["zone"])
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = []

    return clusters

def stability_index(variance):
    return 1 / (np.mean(variance) + 1e-5)

def final_decision(max_risk, stability):
    if max_risk < 4:
        return "System Stable"
    elif max_risk < 5:
        return "Moderate Risk"
    elif stability < 0.1:
        return "High Corruption Risk"
    else:
        return "Critical Failure"

def main():
    zones, roll = get_user_input()

    data = generate_data(zones)
    data = personalize_data(data, roll)

    print("\nBEFORE MUTATION:")
    print(data[0])

    assign, shallow, deep = create_copies(data)

    mutate_data(shallow)

    print("\nAFTER MUTATION:")
    print(data[0])   # shows corruption

    df = to_dataframe(data)
    print("\nDataFrame:\n", df)

    mean, var, corr = analyze(df)

    anomalies = detect_anomalies(df)
    clusters = detect_clusters(df)

    stability = stability_index(var)

    max_risk = df["risk"].max()
    min_risk = df["risk"].min()

    decision = final_decision(max_risk, stability)

    print("\nCorrelation:", corr)
    print("\nAnomalies:\n", anomalies)
    print("\nClusters:", clusters)

    print("\nSummary Tuple:")
    print((max_risk, min_risk, stability))

    print("\nFinal Decision:", decision)


if __name__ == "__main__":
    main()