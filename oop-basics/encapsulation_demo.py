class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def show_balance(self):
        print("Balance: ", self.__balance)

    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        if amount>0 and amount<=self.__balance:
            self.__balance -= amount
            print("Withdraw successful!")
        else:
            print("Invalid withdrawal amount!")

account1 = BankAccount(
    "Kaveh", 
    1000
    )

account1.show_balance()
account1.deposit(500)
account1.show_balance()
account1.withdraw(300)
account1.show_balance()
account1.withdraw(5000)
account1.show_balance()
