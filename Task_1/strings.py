#  1. String Length, Uppercase, Lowercase

sentence = input("Enter a sentence: ")

print("\nSentence Information:")
print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())


# 2. Full Name using f-string


first = input("\nEnter your first name: ")
last = input("Enter your last name: ")

print(f"Full name: {first} {last}")



# 3. Reverse a Word


word = input("\nEnter a word: ")

print("Reversed word:", word[::-1])


# 4. Count the Letter 'a'

sentence2 = input("\nEnter another sentence: ")

count = sentence2.count("a")

print("The letter 'a' appears", count, "times.")