#Challenge 25- Create a text file, write several lines into it, reopen it, and display its contents.
file = open("notes.txt", "w")
file.write("Hello, this is line one. \n")
file.write("This is line two.\n")
file.write("this is line three.\n")
file.close()

file = open("notes.txt", "r")

for line in file:
    print(line, end="")

file.close()
