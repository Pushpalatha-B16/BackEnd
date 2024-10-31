
"""
10)Define an abstract base class Payment with an abstract method pay. Create
two subclasses CreditCardPayment and PayPalPayment that implement the pay method."""

from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,pay_type,pin):
        pass
class CreditCardPayment(Payment):
    def pay(self,pay_type,pin):
            print(f"card or online:{pay_type}")
            d_pin=1234
            if pin==d_pin:
                print("Enter amount:")
                print("payment success")
            else:
                print("payment Failure")
class PayPalPayment(Payment):
    def pay(self,pay_type,pin):
            print(f"card or online:{pay_type}")
            d_pin=2345
            if pin==d_pin:
                print("Enter amount:")
                print("payment success")
            else:
                print("payment Failure")

c=CreditCardPayment()
c.pay("card",2344)
p=PayPalPayment()
p.pay("online",2345)
