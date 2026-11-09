#Challenge 23- Find the first date appearing in a paragraph. Support at least three different date formats

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def clean(word):
    return word.strip(".,;:!?()\"'")

def is_slash_date(word):
    # format: 25/12/2024
    parts = word.split("/")
    if len(parts) != 3:
        return False
    day = parts[0]
    month = parts[1]
    year = parts[2]
    return day.isdigit() and month.isdigit() and year.isdigit() and len(year) == 4

def is_dash_date(word):
    # format: 2024-12-25
    parts = word.split("-")
    if len(parts) != 3:
        return False
    year = parts[0]
    month = parts[1]
    day = parts[2]
    return day.isdigit() and month.isdigit() and year.isdigit() and len(year) == 4

def find_first_date(paragraph):
    words = paragraph.split()
    for i in range(len(words)):
        word = clean(words[i])

        if is_slash_date(word):
            return word

        if is_dash_date(word):
            return word

        # format: December 25, 2024 (this one uses three words in a row)
        if word.capitalize() in months and i + 2 < len(words):
            day = clean(words[i + 1])
            year = clean(words[i + 2])
            if day.isdigit() and year.isdigit() and len(year) == 4:
                return word + " " + day + ", " + year

    return ""


print("Enter your paragraph. Type END on a new line when you are finished.")

paragraph = ""
while True:
    typed = input()
    if typed == "END":
        break
    paragraph = paragraph + typed + "\n"

result = find_first_date(paragraph)

if result == "":
    print("No date found.")
else:
    print(f"First date found: {result}")
