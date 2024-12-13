
word = input("Enter a word: ")

vowels = "aeiouAEIOU"

found_vowels = [char for char in word if char in vowels]

print("Vowels in the word:", found_vowels)