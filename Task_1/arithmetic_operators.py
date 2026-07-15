# 1. Take two numbers from the user and print the result of +, -, *, /, // (floor division), % (modulus), and ** (power).
# 2. Write a program that checks if a number entered by the user is even or odd using the modulus operator.
# 3. Create two boolean variables and print the result of and, or, and not on them.


# Take two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
print("Arithmetic Operations:")
print("Addition (+):", num1 + num2)
print("Subtraction (-):", num1 - num2)
print("Multiplication (*):", num1 * num2)
print("Division (/):", num1 / num2)
print("Floor Division (//):", num1 // num2)
print("Modulus (%):", num1 % num2)
print("Power (**):", num1 ** num2)


# 2. Write a program that checks if a number entered by the user is even or odd using the modulus operator.


num = int(input("Enter the  nmber to check it is even or odd: "))

if num % 2 == 0:
    print(num, "is Even.")
else:
    print(num, "is Odd.")


# 3. Create two boolean variables and print the result of and, or, and not on them.

bool1 = True
bool2 = False

print("\nBoolean Operations:")
print( bool1)
print( bool2)

print("bool1 and bool2 =", bool1 and bool2)
print("bool1 or bool2 =", bool1 or bool2)
print("not bool1 =", not bool1)
print("not bool2 =", not bool2)
