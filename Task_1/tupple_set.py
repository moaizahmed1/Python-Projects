# ## Section 8 — Tuples and Sets

# 1. Create a tuple with three values (name, age, city). Print each value and try to change one value — observe the error and write a one-line comment explaining why it happens.
# 2. Create two sets of numbers and print their union, intersection, and difference.
# 3. Take a list with duplicate values and use a set to remove the duplicates.




# 1. Tuple


person = ("Moaiz", 24, "Lahore")

print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])


# 2: sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)


# 3. Remove Duplicates


numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

unique_numbers = list(set(numbers))

print("\nOriginal List:", numbers)
print("Without Duplicates:", unique_numbers)