"""9)Create an abstract base class BankAccount with abstract methods deposit,
withdraw, and get_balance. Implement these methods in a subclass SavingsAccount."""

from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self,d_amount):
        pass
    @abstractmethod
    def withdraw(self,w_amount):
        pass
    @abstractmethod
    def get_balance(self):
        pass
class SavingsAccount(BankAccount):
    def __init__(self):
       self.amount=1000
    def deposit(self,d_amount):
        print("Before deposit:",self.amount)
        print("After deposit:",self.amount+d_amount)
        self.amount+=d_amount
    def withdraw(self,w_amount):
        if w_amount<=self.amount:
            print("withdraw the amount")
            print("Current amount after wthdraw",self.amount-w_amount)
            self.amount-=w_amount
        else:
            print("Insufficient balance")
            
    def get_balance(self):
          print("Balance:",self.amount)
s= SavingsAccount()
s.deposit(5000)
s.withdraw(1000)
s.get_balance()






















