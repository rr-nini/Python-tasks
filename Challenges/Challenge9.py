#Challenge 9- Ask for a number and determine whether it is odd or even.
num = int(input("Enter a number: "))
remainder = num % 2

if remainder == 0:
    print("Your number is even !")
else:
    print("Your number is odd !")
    