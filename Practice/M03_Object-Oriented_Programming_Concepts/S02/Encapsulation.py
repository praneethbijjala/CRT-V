'''
Encapsulation : Binding data and methods together as a single unit

Access specifiers:
1. public(name)
2. protected(_name)
3. private(__name)

Data hiding can be done using private members
'''
class A:
    a = 10
    _b = 20
    __c = 30

obj = A()
print(obj.a)
print(obj._b)
print(obj._A__c)

#Update a private member
class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def credit(self,amount):
        self.__balance += amount
    def debit(self,amount):
        self.__balance -= amount
    def view(self):
        print("Total amount:",self.__balance)
b = Bank(1000)
b.view()
b.credit(1500)
b.debit(500)
b.view()