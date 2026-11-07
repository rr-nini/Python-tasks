#Challenge 13- Ask for a word and determine whether it is a palindrome. 
word = input("Give me a word and I will determine wether it is a palindrome or not: ")

case = word.lower()

if case == case[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
