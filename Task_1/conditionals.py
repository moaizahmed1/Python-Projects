
# 1. Grade Calculator

marks = float(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")


# 2. Positive, Negative, or Zero

number = float(input("\nEnter a number: "))

if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")


# 3. Age Category

age = int(input("\nEnter your age: "))

if age < 13:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")