#Challenge 4- Ask the user for their birth year and calculate their approximate age. 
year = int(input("What is your birth year?(ex: 2013)"))
current_year = int(input("What is the current year(ex:2026)"))
calc_age = (current_year - year)
print("Your calculated approx age is: " + str(calc_age))