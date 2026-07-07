


# 1. Write a lambda function that takes a number and returns it doubled. Call it with three values.

double = lambda num: num * 2

print(double(5))
print(double(10))
print(double(20))


# 2. Use map() with a lambda to convert a list of temperatures in Celsius to Fahrenheit.


celsius = [0, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)


# 3. Use filter() with a lambda to keep only the numbers greater than 10 from a list.

numbers = [5, 8, 10, 12, 15, 20]

greater_than_10 = list(filter(lambda num: num > 10, numbers))

print(greater_than_10)


# 4. Rewrite task 2 and task 3 above as list comprehensions. Write a one-line comment on which version you find more readable and why.

# I find list comprehensions more readable because they clearly show the transformation and filtering in a single, easy-to-read expression.

celsius = [0, 20, 30, 40]

fahrenheit = [(c * 9/5) + 32 for c in celsius]

print(fahrenheit)



numbers = [5, 8, 10, 12, 15, 20]

greater_than_10 = [num for num in numbers if num > 10]

print(greater_than_10)