#Challenge 24- Ask the user for a filename and determine whether it represents a PDF file. 
def is_pdf(filename):
    last3 = ""
    count = 0
    for char in reversed(filename):    
        if count == 3:
            break                      
        last3 = char + last3           
        count = count + 1
    if last3.lower() == "pdf":
        return True
    return False


filename = input("Enter a filename: ")

if is_pdf(filename):
    print("It is a PDF file.")
else:
    print("It is NOT a PDF file.")