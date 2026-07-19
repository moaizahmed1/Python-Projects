import random

class Account:
    def __init__(self, account_id, name, balance, saving_acount):
        self.account_id = account_id
        self.owner = name
        self.__balance = balance  
        self.saving_acc = saving_acount

    def debit(self, amount):
        if self.saving_acc:
            if (self.__balance - amount) >= 500:
                self.__balance -= amount
                print("remianinhg balance",self.get_balance())
                return True
            print("Transaction failed: Savings requires 500 minimum balance.")
            return False
        if amount <= 0:
            print ("Amount must be Positive")  
            self.__balance -= amount
            return True
        print("Insufficient balance")
        return False

    def credit(self, amount):
        self.__balance += amount
        return True

    def get_balance(self):  
        return self.__balance
class Branch:
    def __init__(self, branch_name):
        self.branch = branch_name
        self.account = {}

    def add_account(self, account_id, name, balance, savings_account):
        self.account[account_id] = Account(account_id, name, balance, savings_account)
    
    def del_account(self, account_id):
        return self.account.pop(account_id, None)
    
    def update_name(self, account_id, new_name):
        if account_id in self.account:
            self.account[account_id].owner = new_name
            return True
        return False   
class BankSystem:
    def __init__(self):

        self.data = {
            "1": {"name": "Islamabad", "branches": {"1": Branch("F-9"), "2": Branch("Faizabad")}},
            "2": {"name": "Lahore", "branches": {"1": Branch("Gulberg")}},
            "3": {"name": "Karachi", "branches": {"1": Branch("Clifton")}}
        }
               

    def manage_branches(self):
        print("\nBranch CRUD")
        print("1: Add Branch | 2: Delete Branch")
        choice = input("Choice: ")
        city_id = input("Enter City ID: ")
        if city_id not in self.data: 
            return
        
        if choice == "1":
            name = input("Branch Name: ")
            new_id = str(len(self.data[city_id]["branches"]) + 1)
            self.data[city_id]["branches"][new_id] = Branch(name)
        elif choice == "2":
            bid = input("Branch ID: ")
            self.data[city_id]["branches"].pop(bid, None)

def main():
    bank = BankSystem()
    
    while True:
        print("\n1: Islamabad | 2: Lahore | 3: Karachi | 4: Manage Branches | 5: Exit")
        city_choice = input("Enter City ID: ")
        
        if city_choice == "5": 
            break
        if city_choice == "4": 
            bank.manage_branches() 
            continue
        if city_choice not in bank.data: 
            continue
        
       
        branches = bank.data[city_choice]["branches"]
        
        
        print(f"\n--- Branches in {bank.data[city_choice]['name']} ---")
        for id_number, branch_obj in branches.items():
            print(f"{id_number}: {branch_obj.branch}")
            
        branch_id = input("Enter Branch ID: ")
        if branch_id not in branches:
            print("Invalid Branch ID.")
            continue
        current_branch = branches[branch_id]

        while True:
            print(f"\n--- Welcome to {current_branch.branch} ---")
            print("1: Add Current Account | 2: Add Savings Account | 3: Actions | 4: Update | 5: Delete | 6: Check All Accounts |7: Back")
            choice = input("Enter Option: ")

            if choice in ["1", "2"]:
                acc_id = str(random.randint(1000, 9999))
                name = input("Name: ")
                bal = int(input("Balance: ") or 0)
                current_branch.add_account(acc_id, name, bal, (choice == "2"))
                print(f'Account created! ID: {acc_id}')

            elif choice == '3':
                acc_id = input('Search ID: ')
                acc = current_branch.account.get(acc_id)
                if acc:
                    op = input('1: Debit | 2: Credit | 3: Balance | 4: Exit: ')
                    if op == "1": 
                        acc.debit(int(input('Amt: ')))
                    elif op == "2": 
                        acc.credit(int(input('Amt: ')))
                    elif op == '3': 
                        print(f'Balance: {acc.get_balance()}')
                else: print("Not found.")

            elif choice == "4":
                if current_branch.update_name(input('ID: '), input("New Name: ")): 
                    print("Updated")
            elif choice == "5":
                if current_branch.del_account(input('ID: ')): 
                    print("Deleted")
            elif choice == "6":
                
                pin = input("Enter Pin to see the accounts: ")
                
                if pin == "1234":
                
                 account = current_branch.account
                
                 if account:
                    print(f"{branch_obj.branch}: {branch_obj.account}")
                 else:
                    print("No accounts found")
                else:
                    print('Wrong Pin')
 
            elif choice == "7": 
                break
main()