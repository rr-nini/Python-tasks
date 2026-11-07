#Challenge 21- Create a reusable program component that receives text and returns the text without extra spaces. 
def remove_extra_spaces(text):
    words = text.split()
    cleaned = " ".join(words)
    return cleaned

userText = input("Enter some text: ")
result = remove_extra_spaces(userText)
print(f"Cleaned text: '{result}'")
