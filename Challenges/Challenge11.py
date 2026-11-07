# Challenge 11- Ask for three numbers and display the largest and smallest numbers. 
num_1 = int(input("Give me your first number: \n"))
num_2 = int(input("Give me your second number: \n"))
num_3 = int(input("Give me your third number: \n"))

largest = max(num_1, num_2, num_3)
smallest = min(num_1, num_2, num_3)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
