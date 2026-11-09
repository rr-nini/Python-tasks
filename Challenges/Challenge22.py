#Challenge 22- #Create a reusable program component that receives a paragraph and returns its first non-empty line
def first_non_empty_line(paragraph):
    line = ""
    for char in paragraph:
        if char == "\n":
            if line != "":
                return line
        elif char == " " and line == "":
            pass
        else:
            line = line + char
    return line


print("Enter your paragraph. Type END on a new line when you are finished.")

paragraph = ""
while True:
    typed = input()
    if typed == "END":
        break
    paragraph = paragraph + typed + "\n"

result = first_non_empty_line(paragraph)

if result == "":
    print("Every line was empty.")
else:
    print(f"First non-empty line: '{result}'")