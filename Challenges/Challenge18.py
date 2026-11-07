#Challenge 18- Accept a list of numbers and display the total, average, highest, and lowest values. 
numbers = []

count = int(input("How many numbers do you want to enter: "))

for i in range(count):
    num = float(input(f"Enter Number {i + 1} : "))
    numbers += [num]

    
total = sum(numbers)
average = total / len(numbers)
highest = max(numbers)
lowest = min(numbers)

print(f"\nTotal: {total}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
