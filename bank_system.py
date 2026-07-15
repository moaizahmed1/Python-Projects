# Create a Python program that manages bank accounts across three different branches.(Create an Account class (to store name and balance) and a Bank class (to store accounts for a specific branch_name)).

# Methods: * Add credit and debit methods to the Account class to update the balance.

# Task:

# Initialize 3 branches (e.g., North, South, East).
# Add different accounts in them.
# Perform a debit on one account and a credit on another.
# Print the final balances to verify the updates.


class Account:
    def __init__(self, name, balance):
        self.owner = name
        self.__balance = balance  

    def debit(self, amount):
        if amount <= self.__balance:  
            self.__balance -= amount
            return True
        else:
            print("Insufficient balance")
            return False

    def credit(self, amount):
        self.__balance += amount
        return True

    def get_balance(self):  
        return self.__balance

    def show_balance(self):
        print("Balance:", self.__balance)


class Bank:
    def __init__(self, branch_name):
        self.branch = branch_name
        self.account = {}

    def add_account(self, name, balance):
        self.account[name] = Account(name, balance)

    def get_account(self, name):
        return self.account.get(name)


def main():
    branches = {
        "1": Bank('Islamabad'),
        "2": Bank('Lahore'),
        "3": Bank('Karachi')
    }
    
    branches["1"].add_account('Moaiz', 1000)
    branches["2"].add_account('Suffyan', 4000)
    branches["3"].add_account('Huzaifa', 5000)

    while True:
        print('--------Banking System--------')
        print('--------Select Branch--------')
        print('1: Islamabad | 2: Lahore | 3: Karachi | 4: Exit')
        
        b_choice = input("Enter any option: ")  
        
        if b_choice == "4":  
            print("Thanks for using our app")
            break
        if b_choice not in branches:
            print("Invalid branch choice.")
            continue
            
        current_branch = branches[b_choice]
        name = input("Enter name: ")
        account = current_branch.get_account(name)
        
        if not account:
            print("No account found")
            continue

        print(f"\n1: Debit | 2: Credit | 3: Show Balance | 4: Back")
        option = input("Choose Option: ")

        if option == "1":  
            amt = int(input("Amount: "))
            if account.debit(amt):
                print("Transaction successful")
            else:
                print("Transaction failed")
                
        elif option == "2":  
            amt = int(input("Amount: "))
            if account.credit(amt):
                print("Amount Credited Successfully")
            else:
                print("Failed")
                
        elif option == "3":
            print(f"Balance: {account.get_balance()}")
            
        elif option == "4":
            print("Retiurining to main menu......")
            continue

main()

    