# ## Section 1 — Comprehensions







# 1. Use a list comprehension to create a list of the squares of numbers from 1 to 10.

squares = [num ** 2 for num in range(1, 11)]
print(squares)



# 2. Use a list comprehension with a condition to get only the even numbers from 1 to 20.




even=[num for num in range(1,21) if num % 2 == 0 ]
print(even)

# 3. Given a list of words, use a comprehension to create a new list with only the words longer than 4 letters.

words=['Mango','Apple','Coco','Moiz','Ali','Happy']

new_list=[word for word in words if len(word) > 4]
print(new_list)


# 4. Use a dictionary comprehension to map numbers 1–5 to their cubes, like {1: 1, 2: 8, 3: 27, ...}.

cubes={num: num ** 3 for num in range(1,6)}

print(cubes)


# 5. Use a set comprehension to get the unique first letters of a list of names.

names = ["Ali", "Ahmed", "Bilal", "Ayesha", "Hamza", "Bilal"]

first_letters = {name[0] for name in names}
print(first_letters)