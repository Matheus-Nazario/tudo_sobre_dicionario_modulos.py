a_dict = {"color": "blue", "fruit": "apple", "pet": "dog"}

for key, value in a_dict.items():
    print(key, "->", value)

a_dict = {"one": 1, "two": 2, "thee": 3, "four": 4}
new_dict = {}  # Create a new empty dictionary
for key, value in a_dict.items():
    # If value satisfies the condition, then store it in new_dict
    if value <= 2:
        new_dict[key] = value

print(new_dict)
