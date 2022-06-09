class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance+amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# account = Account("App_5_GUI_and_SQL_BookInventory//account//balance.txt")
# print(account.balance)
# print(account.balance)
# account.deposit(200)
# account.commit()


class Checking(Account):
    """This class generates cheking account objects"""

    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


vlad_checking = Checking(
    "App_5_GUI_and_SQL_BookInventory//account//vlad.txt", 1)
vlad_checking.transfer(10)
print(vlad_checking.balance)
vlad_checking.commit()
print(vlad_checking.type)

john_checking = Checking(
    "App_5_GUI_and_SQL_BookInventory//account//john.txt", 1)
john_checking.transfer(10)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)


print(john_checking.__doc__)
