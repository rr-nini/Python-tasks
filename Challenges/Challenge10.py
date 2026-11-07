# Challenge 10- Ask for a person’s age and classify them as a child, teenager, adult, or senior. 
num = int(input("Enter your age(ex.12) : "))

if num <= 12 and num >= 0 :
    print("You are a child!")
elif num <= 19 and num >= 13 :
    print("You are a teenager !")
elif num >=19 and num <= 60 :
    print("You are an adult !")
else :
    print("Your are a senior !")
