
# 1. Greeting Function


def greet(name):
    return f"Hello, {name}!"

print(greet("Moaiz"))
print(greet("Ali"))
print(greet("Sara"))



# 2. Addition Function


def add(a, b):
    return a + b

# Calling the function
result = add(10, 20)
print("\nSum:", result)



# 3. Check if Number is Even


def is_even(number):
    return number % 2 == 0


print("\nIs 8 even?", is_even(8))
print("Is 15 even?", is_even(15))



# 4. Area of Rectangle


def area_of_rectangle(length, width=1):
    return length * width

# Calling the function
print("\nArea (length=10, width=5):", area_of_rectangle(10, 5))
print("Area (length=10):", area_of_rectangle(10))


# 5. Factorial Function


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print("\nFactorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))