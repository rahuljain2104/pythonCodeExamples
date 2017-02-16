from abc import ABCMeta, abstractmethod


# abstraction
# polymorphism
# inheritance
# data encapsulation

class Customer:
    '''
    This is a bank customer, and will
    be ble to do the transactions
    '''

    __metaclass__ = ABCMeta

    has_nearby_atm = True

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if (self.balance >= amount) and (amount > 0):
            self.balance -= amount
            return "withdrawn successfully, current balance : " + str(self.balance)
        else:
            return "Amount is greater than balance, so cannot withdrawn"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "current balance : " + str(self.balance)
        else:
            return "wrong amount entered !!!"

    @staticmethod
    def my_bank_name():
        print("State Bank of India")

    @classmethod
    def my_bank_address(cls):
        return cls.has_nearby_atm

    @abstractmethod
    def customer_type(self):
        """"Return a string representing the type of customer this is."""
        pass


class PremiumCustomer(Customer):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.__account_type = None

    @property
    def account_type(self):
        return self.__account_type

    @account_type.setter
    def account_type(self, acc_type):
        self.__account_type = acc_type

    def customer_type(self):
        print("{} is a premium customer".format(self.name))


class ValuedCustomer(Customer):
    def __init__(self, name, balance, account_type="Valued"):
        super().__init__(name, balance)
        self.account_type = account_type

    @property
    def account_type(self):
        return self.__account_type

    @account_type.setter
    def account_type(self, acc_type):
        self.account_type = acc_type

    def customer_type(self):
        print("{} is a valued customer".format(self.name))


premium_customer = PremiumCustomer("Rahul", 5000)

print(premium_customer.name)
premium_customer.account_type = "Double premium account"
print(premium_customer.account_type)
premium_customer.customer_type()
