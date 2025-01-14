class Math_operations:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(Math_operations.add(3, 5))
print(Math_operations.multiply(3, 5))


# Example 2

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

account = BankAccount(1000)
print(account.balance)
account.balance = 500
print(account.balance)

