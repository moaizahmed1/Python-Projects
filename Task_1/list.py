
# 1. Create a list of 5 fruits. Print the first fruit, the last fruit, and the whole list.
# 2. Add a new fruit to the end of the list, remove the second fruit, then print the updated list.
# 3. Take 5 numbers from the user, store them in a list, and print the largest, the smallest, and the sum.
# 4. Given the list [4, 1, 7, 3, 9, 2], sort it in ascending order and then in descending order.
# 5. Loop through a list of names and print each name with its position number (use enumerate()).



# 1. Create and Access a List


fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Complete list:", fruits)



# 2. Modify the List

fruits.append("Pineapple")   # Add a new fruit
fruits.pop(1)                # Remove the second fruit (Banana)

print("\nUpdated fruit list:")
print(fruits)


# 3. Take 5 Numbers from the User


numbers = []

print("\nEnter 5 numbers:")

for i in range(5):
   num = float(input("Enter number " + str(i + 1) + ": "))
   numbers.append(num)

print("\nNumbers:", numbers)
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
print("Sum:", sum(numbers))



# 4. Sort a List


num_list = [4, 1, 7, 3, 9, 2]

# Ascending order
num_list.sort()
print("\nAscending order:", num_list)

# Descending order
num_list.sort(reverse=True)
print("Descending order:", num_list)



# 5. Loop with enumerate()


names = ["Moaiz", "Ali", "Ahmed", "Sara", "Ayesha"]

print("\nNames with Position:")

for index, name in enumerate(names, start=1):
    print(f"this is index {index} this is name: {name}")
    


