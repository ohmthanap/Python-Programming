# Thanapoom Phatthanaphan
# This is a program to represents a savings account with the owner's name, PIN, and balance.
# And also to let the user select an option to operate user's account.

class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        result = 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """If the amount is valid, substract it
        from the balance and returns None;
        otherwise, returns an error message."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __eq__(self, other):
        """Returns True if names are equal or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.name == other.name

    def __lt__(self, other):
        """Returns True if name of self is less than
        name of other, or False otherwise."""
        return self.name < other.name

account = SavingsAccount("Kevin", "1234", 10000)

print(account.__str__())
print()
while True:
    owner_action = input("What do you want to do with your account?\n"
    "Enter 1: Deposit\nEnter 2: Withdraw\nEnter 3: Check Balance\n"
    "Enter 4: End the program\n")
    if owner_action == '1':
        deposit = input("How much do you want to deposit: ")
        account.deposit(int(deposit))
        print()
    elif owner_action == '2':
        withdraw = input("How much do you want to withdraw: ")
        account.withdraw(int(withdraw))
        print()
    elif owner_action == '3':
        print(account.getBalance())
        print()
    elif owner_action == '4':
        break
    else:
        print("You entered a wrong number, please re-enter a number by following")
        print()
        continue

print("You account balance is " + str(account.getBalance()))
account.computeInterest() # Add interest
print("You account balance after 1 year of saving with interest rate at 2% is " + str(account.getBalance()))
print()

account_2 = SavingsAccount("Tony", "5678")
print(account.__eq__(account_2))
print(account.__lt__(account_2))
print()

account_3 = SavingsAccount("Steven", "1357", 50000)
print(account.__eq__(account_3))
print(account.__lt__(account_3))