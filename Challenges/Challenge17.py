#Challenge 17- Accept five names from the user, store them together, and display them alphabetically. 
names = []

for i in range(5):
    name  = input(f"Give me name {i + 1} :")
    names += [name]
    
sorted_names = sorted(names)

print("\n names in alphabetical order: \n")
for name in sorted_names:
    print(f"\n {name} ")
    