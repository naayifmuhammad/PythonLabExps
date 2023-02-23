# 4. Define a class to represent a bank account. Include the following details like name of the
# depositor, account number, type of account, balance amount in the account. Write methods
# to assign initial values, to deposit an amount, withdraw an amount after checking the
# balance, to display details such as name, account number, account type and balance.

class BankAccount:
    def __init__(self,acName,acNo,acType):
        self.acName = acName
        self.acNo = acNo
        self.acType = acType
        self.acBalance = 0
    def accountDetails(self):
        print(f"Account details of {self.acName}:\n\n")
        print(f"Account No: {self.acNo}")
        print(f"Account Holder Name: {self.acName}")
        print(f"Account Type: {self.acType}")
        print(f"Account Balance: {self.acBalance}")
   
    def currentBalance(self):
        return self.acBalance
    
    def withdraw(self):
        amount = int(input(f"\nEnter the amount you want to withdraw [Current balance {self.currentBalance()}]:  "))
        if amount<=self.currentBalance():
            self.acBalance -= amount
            print(f"\nAmount [{amount}] withdrawn from AC No:{self.acNo}: Current balance is: {self.currentBalance()}")
        else:
            print("Cannot withdraw that amount: Amount exceeds balance")
    def deposit(self):
        amount = int(input(f"\nEnter the amount you wish to deposit to your account: "))
        self.acBalance += amount
        print(f"\nAmount [{amount}] credited to AC No:{self.acNo}: Current balance is: {self.currentBalance()}")
    


        
def displayMenu():
    print("\n0.Exit 1.Create new account 2.Deposit 3.Check Balance 4.Withdraw 5.Account details 6.Choose another account\n")

def switchAccount():
    print("Choose your account: \n")
    print(f"AC No  |  AC Name:\n")
    for account in accountsList.values():
        print(f"{account.acNo}      {account.acName}")
    acToSwitchTo = int(input("Enter the account no of your choice: "))
    currentAccount = 0 
    if acToSwitchTo in accountsList.keys():
        currentAccount = accountsList[acToSwitchTo]
        print(f"Welcome {currentAccount.acName}")
        return currentAccount
    else:
        print("\nPlease enter a valid account No from the list\n")
        


        

accountsList = {}
newAccount = 0
choice = -1
while choice!=0:
    displayMenu()
    choice = int(input("Which operation do you want to perform: "))
    if choice == 1 :
        acName = input("Enter account holder name: ")
        acNo = int(input("Enter account number: "))
        acType = input("Enter account type: ")
        newAccount = BankAccount(acName,acNo,acType)
        accountsList[acNo] = newAccount
        newAccount.accountDetails()
    if choice == 2:
        newAccount.deposit()
    if choice ==3:
        print(f"Current balance : {newAccount.currentBalance()}")
    if choice == 4:
        newAccount.withdraw()
    if choice == 5:
        newAccount.accountDetails()
    if choice == 6:
        newAccount = switchAccount()
    


    