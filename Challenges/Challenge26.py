#Challenge 26- Ask the user for a file path and display its filename, extension, size, and location. 
import os

def show_file_info(path):
    if not os.path.isfile(path):
        print("That file does not exist.")
        return

    fullPath = os.path.abspath(path)
    filename = os.path.basename(fullPath)
    location = os.path.dirname(fullPath)              
    name, extension = os.path.splitext(filename)
    size = os.path.getsize(fullPath)

    print(f"Filename:  {filename}")
    print(f"Extension: {extension}")
    print(f"Size:      {size} bytes")
    print(f"Location:  {location}")


path = input("Enter a file path: ")
show_file_info(path)