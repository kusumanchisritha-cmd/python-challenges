import copy

# -----------------------------
# STEP 1: USER INPUT DATA
# -----------------------------
def generate_data():
    users = []
    n = int(input("Enter number of users: "))

    for i in range(n):
        print(f"\nUser {i+1}")

        file_count = int(input("Enter number of files: "))
        files = []

        for j in range(file_count):
            f = input(f"Enter file {j+1}: ")
            files.append(f)

        usage = int(input("Enter usage: "))

        users.append({
            "id": i+1,
            "data": {
                "files": files,
                "usage": usage
            }
        })
    return users


# -----------------------------
# STEP 2: REPLICATION
# -----------------------------
def replicate_data(users):
    assigned = users
    shallow = copy.copy(users)
    deep = copy.deepcopy(users)
    return assigned, shallow, deep


# -----------------------------
# STEP 3: MODIFY DATA
# -----------------------------
def modify_data(data, roll):
    for user in data:
        user["data"]["usage"] += 50

        if roll % 2 == 0:
            user["data"]["files"].append("new.txt")
        else:
            if len(user["data"]["files"]) > 0:
                user["data"]["files"].pop()

    return data


# -----------------------------
# STEP 4: CHECK INTEGRITY
# -----------------------------
def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0
    overlap = 0

    for i in range(len(original)):
        orig = set(original[i]["data"]["files"])
        sh = set(shallow[i]["data"]["files"])
        dp = set(deep[i]["data"]["files"])

        if orig != dp:
            leakage += 1

        if dp != sh:
            safe += 1

        overlap += len(orig.intersection(sh))

    return leakage, safe, overlap


# -----------------------------
# MAIN
# -----------------------------
users = generate_data()

print("\n--- BEFORE ---")
print(users)

assigned, shallow, deep = replicate_data(users)

roll_no = int(input("\nEnter your roll number: "))

shallow = modify_data(shallow, roll_no)

print("\n--- AFTER ---")

print("\nOriginal Data:")
print(users)

print("\nShallow Copy:")
print(shallow)

print("\nDeep Copy:")
print(deep)

result = check_integrity(users, shallow, deep)

print("\nIntegrity Report (leakage, safe, overlap):")
print(result)

print("\nData Corruption:")
print("Original data changed due to shallow copy sharing inner data.")