#Challenge 19-  Remove duplicate values from a collection of names while preserving the original order.
names_input = input("Enter names separated by commas: ")
original_names = names_input.split(",")

# manually strip spaces from each name without using .strip()
names = []
for original_name in original_names:
    cleaned = ""
    for char in original_name:
        if char != " ":
            cleaned += char
    names.append(cleaned)

new_names = []

for name in names:
    already_have_it = False
    for existing_name in new_names:
        if name == existing_name:
            already_have_it = True
            break
    if not already_have_it:
        new_names.append(name)

print("Unique names (order preserved):", new_names)
