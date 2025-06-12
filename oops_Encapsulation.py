class BankAccount:
    # Constructor to initialize the account
    def __init__(self, owner, balance):
        self.owner = owner              # Public attribute - can be accessed directly
        self.__balance = balance        # Private attribute - should not be accessed directly outside the class

    # Public method to display balance (safe way to access private data)
    def check_balance(self):
        print(f"Available balance for {self.owner}: ₹{self.__balance}")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount} successfully.")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount} successfully.")
        else:
            print("Insufficient balance")

    # Private method 
    def __show_internal_status(self):
        print("This is a private method just for internal checks.")

# Creating an object of BankAccount
acc = BankAccount("rohan", 5000)

# Accessing public method - this is how you're supposed to interact with the class
acc.check_balance()

# Trying to deposit money using a method - good practice
acc.deposit(1500)
acc.check_balance()

# Trying to withdraw money safely through method
acc.withdraw(2000)
acc.check_balance()

# Trying to access private variable directly - not recommended
# This will raise error: AttributeError: 'BankAccount' object has no attribute '__balance'

#  Python allows access using name mangling (not recommended, just for learning)
print("Accessing private balance unethically:", acc._BankAccount__balance)

# now i am Trying to call private method directly - also it is possible using name mangling
acc._BankAccount__show_internal_status()
