
# class Shape:
#     def __init__(self, d1, d2):
#         self.dimension1 = d1
#         self.dimension2 = d2
#     def area(self):
#         return self.dimension1 * self.dimension2
#     def display(self):
#         print(f"Dimension1: {self.dimension1}\n Dimension2: {self.dimension2}")
    
# class Recatangle(Shape):
#     pass


# rectangle = Recatangle(5, 20)
# area = rectangle.area()
# print(F'The area of the rectangle is : {area} ')


from abc import ABC, abstractmethod

class InternationalCreditCard(ABC):
    @abstractmethod
    def rupees(self):
        pass
    @abstractmethod
    def dollars(self):
        pass
    @abstractmethod
    def pounds(self):
        pass


class BankAccount(InternationalCreditCard):
    def __init__(self, balance_in_rupees):
        self.balance_in_rupees = balance_in_rupees
    def rupees(self, deduction):
        self.balance_in_rupees = self.balance_in_rupees - deduction
        print(f'Deducted {deduction} Rupees')
    def dollars(self, deduction, dollar_exchange_rate = 72):
        self.balance_in_rupees = self.balance_in_rupees - (deduction * dollar_exchange_rate)
        print(f'Deducted {deduction * dollar_exchange_rate} Dollars')
    def pounds(self, deduction, pound_exchange_rate = 93):
        self.balance_in_rupees =  self.balance_in_rupees - (deduction * pound_exchange_rate)
        print(f'Deducted {deduction * pound_exchange_rate} Pounds')
    def get_money(self):
        print(f"Balance: Rs.{self.balance_in_rupees}")
    

current_bank_ac = BankAccount(3550)
current_bank_ac.get_money()

current_bank_ac.rupees(10)
current_bank_ac.dollars(10)
current_bank_ac.pounds(10)
current_bank_ac.get_money()

