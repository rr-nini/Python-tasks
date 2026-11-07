#Challenge 15- Find how many times a particular word appears in a paragraph. 
sentence = input("Enter a paragraph: ")
search_word = input("Enter a word to search for: ")
clean_words = sentence.lower().split()
search_word_clean = search_word.lower()

count = 0

for word in clean_words:
    cleaned_word = word.strip(".,!?;:\"'()")
    if cleaned_word == search_word_clean:
        count += 1
print(f"{search_word} appears: {count} amount of time(s) in the paragraph!")
