energy_readings=[45, 120, 200, 30, 75, 180, -5, 60, 15, 250]
categorized={
    "efficient":[],
    "moderate":[],
    "high":[],
    "invalid":[]
}
for e in energy_readings:
       if e<0:
           categorized["invalid"].append(e)
       elif  0 <= e <= 50:
               categorized["efficient"].append(e)
       elif 51<=e<=150:
               categorized["moderate"].append(e)
       else:
           categorized["high"].append(e)
valid_readings=[e for e in energy_readings if e>=0]
summary=(
    len(energy_readings),
    sum(valid_readings),
    len(categorized["efficient"]),
    len(categorized["moderate"]),
    len(categorized["high"]),
    len(categorized["invalid"]),
)
result=[]
if len(categorized["high"])>3:
    result.append("Overconsumption")
if len(categorized["efficient"])-len(categorized["moderate"])<=1:
    result.append("Balanced Usage")
if  sum(valid_readings)>600:
    result.append("Energy waste Detected")
print("Display:")

print("\nCategorized Readings:")
for key in categorized:
    print(f"{key.capitalize()}: {categorized[key]}")

print(f"\nTotal Consumption: {summary[0]}")
print(f"Number of Buildings: {summary[1]}")

print("\nEfficiency Result:")
if result:
    for res in result:
        print(res)
else:
    print("Efficient Campus")
