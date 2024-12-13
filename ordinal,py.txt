
word = input("Enter a word: ")

print("Ordinal values of the characters:")
for char in word:
    print(f"{char}: {ord(char)}")