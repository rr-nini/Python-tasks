#Challenge 16- Display every number from 1 to 100 that is divisible by both 3 and 5.
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
