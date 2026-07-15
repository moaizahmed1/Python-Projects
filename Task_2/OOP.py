
# ## Section 6 — Object-Oriented Programming (the big one)





# ### 6a — Classes and objects
# 1. Create a class Dog with attributes name and breed set in __init__. Create two dog objects and print their names.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.name)
print(dog2.name)

# 2. Add a method bark() to the Dog class that prints <name> says Woof!. Call it on both objects.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says Woof!")


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

dog1.bark()
dog2.bark()

# 3. Create a class BankAccount with:
#    - an __init__ that takes an owner and sets balance to 0
#    - a deposit(amount) method
#    - a withdraw(amount) method that refuses to withdraw more than the balance
#    - a show_balance() method
class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.balance)


# 4. Create an account, deposit some money, withdraw some, try to over-withdraw, and watch it behave.


account = BankAccount("Moaiz")

account.deposit(1000)
account.show_balance()

account.withdraw(300)
account.show_balance()

account.withdraw(1000)
account.show_balance()



# ### 6c — Inheritance
# 5. Create a class Animal with a method speak() that prints Some sound. Create two child classes Cat and Cow that override speak() with their own sounds.

class Animal:

    def speak(self):
        print("Some sound")


class Cat(Animal):

    def speak(self):
        print("Meow")


class Cow(Animal):

    def speak(self):
        print("Moo")

# 6. Create one Cat and one Cow, put them in a list, loop through it, and call speak() on each. (This is polymorphism: same method name, different behavior.)

cat = Cat()
cow = Cow()

animals = [cat, cow]

for animal in animals:
    animal.speak()




# ### 6d — Encapsulation
# 7. In your BankAccount class, make balance "private" by naming it _balance, and force all changes to go through the methods. Write a one-line comment on why exposing balance directly would be a bad idea.


class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self._balance)

    