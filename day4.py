data_input = input("data: ")
cleaned = ""
for ch in data_input:
    if ch != "[" and ch != "]":
        cleaned = cleaned + ch
items = cleaned.split(",")
data = []
for item in items:
    value = item.strip()
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    if value != "":
        if value.isdigit():
            data = data + [int(value)]
        else:
            data = data + [value]

number_list = []
string_list = []
for i in data:
    if type(i) == int:
        number_list = number_list + [i]
    else:
        string_list = string_list + [i]

total_numbers = 0
for n in number_list:
    total_numbers = total_numbers + 1

total_strings = 0
for s in string_list:
    total_strings = total_strings + 1

name = input("Enter your name: ")
name_length = 0
for ch in name:
    name_length = name_length + 1
if len(name) % 2 == 0:
    new_numbers = []
    index = 0
    for n in number_list:
        if index != 0:
            new_numbers = new_numbers + [n]
        index = index + 1
    number_list = new_numbers

    new_strings = []
    index = 0
    for s in string_list:
        if index != 0:
            new_strings = new_strings + [s]
        index = index + 1
    string_list = new_strings
else:
    new_numbers = []
    index = 0
    for n in number_list:
        if index != total_numbers - 1:
            new_numbers = new_numbers + [n]
        index = index + 1
    number_list = new_numbers

    new_strings = []
    index = 0
    for s in string_list:
        if index != total_strings - 1:
            new_strings = new_strings + [s]
        index = index + 1
    string_list = new_strings
print("Numbers List:", number_list)
print("Strings List:", string_list)
print()
print("Total Numbers:", total_numbers)
print("Total Strings:", total_strings)
