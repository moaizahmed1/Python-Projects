# ## Section 5 — Modules and Packages

# 1. Create a file mathutils.py with two functions: add(a, b) and multiply(a, b).
# 2. In a separate file main.py, import mathutils and use both functions.
# 3. Import only the add function using from mathutils import add and use it.
# 4. Import the built-in random module and write a program that picks a random number between 1 and 100.
# 5. Import the built-in datetime module and print today's date in the format DD-MM-YYYY.




# 3. Import only the add function using from mathutils import add and use it.


import mathutils

sum_numbers=mathutils.add(4,5)
print(sum_numbers)

# 4. Import the built-in random module and write a program that picks a random number between 1 and 100.


import random

random_number=random.randint(1,100)

print(random_number)

# 5. Import the built-in datetime module and print today's date in the format DD-MM-YYYY.


import datetime

todays_date=datetime.date.today()
print(todays_date)