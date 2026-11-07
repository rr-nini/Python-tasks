#Challenge 7- Ask for three marks and calculate their total and average. 
mark_1 = int(input("Give me your first mark: \n"))
mark_2 = int(input("Give me your second mark: \n"))
mark_3 = int(input("Give me your third mark: \n"))
total = (mark_1 + mark_2 + mark_3)
avg = (total / 3)

print(f"Your total is: {total} and your avg is:  {avg:.3}")
