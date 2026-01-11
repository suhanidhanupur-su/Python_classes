# Accessing List inside Dictionary
my_dict = {
    "name": ["Ujwal", "Ravi", "Rahul"],
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(my_dict["name"])
print(my_dict["name"][1])  # Ravi
# ==================================================
my_dict = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(my_dict)
print(my_dict.keys())
# ====================================================
diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(diwakar_dictionary)
print(diwakar_dictionary.values())
# ====================================================
diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(diwakar_dictionary.get("name"))

# ====================================================
diwakar_dictionary = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

diwakar_dictionary.update({"roll_no": 251})
print(diwakar_dictionary)




{'name': 'Ujwal', 'age': 24, 'city': 'Bangalore', 'roll_no': 251}

# ====================================================


