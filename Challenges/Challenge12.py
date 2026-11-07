#Challenge 12- Ask for a sentence and display the number of characters and words it contains. 
sentence = input("Enter a sentence: ")
num_chrs = len(sentence)
num_words = len(sentence.split())

print(f"Your sentence has {num_chrs} characters and {num_words} words.")
