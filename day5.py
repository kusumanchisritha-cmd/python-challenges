weights_input = input("Input Weights: ")
weights = []
num = ""

for ch in weights_input:
    if ch != " " and (ch.isdigit() or ch == "-"):
        num += ch
    else:
        if num != "":
            weights.append(int(num))
            num = ""
if num != "":
    weights.append(int(num))
name = input("Enter your full name: ")
L = 0
for ch in name:
    if ch != " ":
        L = L + 1
print("Length without spaces:", L)
PLI = L % 3
total_valid = 0
total_invalid = 0
invalid=[]
overload=[]
print("\nOutput:")

for m in weights:
    if m<0:
        invalid.append(m)
        total_invalid +=1
    elif 0 <= m <= 5:
            print(m,"->Light weight")
            total_valid +=1
    elif 6 <= m <= 25:
            print(m,"->Normal weight")
            total_valid +=1
    elif 26 <= m <= 60:
            print(m,"->Heavy load")
            total_valid +=1
    else:
        print(m,"->Overload")
        overload.append(m)
print("Total Valid Marks:", total_valid)
print("Total Invalid Marks:", total_invalid)
if PLI==0:
    print("L:", L)
    print("PLI:", PLI)
    for item in overload:
        invalid.append(item)
    overload = []
    print("After moving overload items to invalid:",invalid)
elif PLI ==1:
    i=0
    while i < len(weights):
        if 0<=weights[i]<=5:
            weights.pop(i)
        else:
            i+=1
    print("L", L)
    print("PLI", PLI)
    print("Final weights:", weights)

elif PLI==2:
    final_weights = []
    for m in weights:
        if 6 <= m <= 60:
            final_weights.append(m)
    print("L:",L)
    print("PLI:",PLI)
    print("(Only Normal and Heavy):", final_weights)

