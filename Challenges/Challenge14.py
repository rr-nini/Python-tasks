#Challenge 14- Count how many vowels and consonants appear in a sentence. 
sentence = input("Enter a sentence: ")
vowel_count = 0
consonant_count = 0
vowels = "aeiou"
clean_sentence = sentence.lower()

for char in clean_sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
