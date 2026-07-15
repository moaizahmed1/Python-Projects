
# 1. Print numbers from 1 to 10

print("Numbers from 1 to 10:")

for i in range(1, 11):
    print(i)



# 2. Multiplication Table

number = int(input("\nEnter a number: "))

print("\nMultiplication Table of:" ,number)

for i in range(1, 11):
    print("number x i =" ,number * i)



# 3. Password Checker


password = ""

while password != "python123":
    password = input("\nEnter the password: ")

print("Access granted")
 
# 4. Print Even Numbers (1 to 50)

print("\nEven numbers from 1 to 50:")

for i in range(2, 51, 2):
    print(i)



# 5. Sum of Numbers from 1 to 100


total = 0

for i in range(1, 101):
    total += i

print("\nSum of numbers from 1 to 100 is:", total)