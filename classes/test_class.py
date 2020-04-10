class BusinessCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
        
    def print_info(self):
        print("--------------------------")
        print("Name: ",self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("--------------------------")

class Foo:
    def func1():
        print("function 1")
    def func2(self):
        print(id(self))
        print("function 2")

class Stock:
    market = "kospi"

class Account:
    num_accounts=0
    def __init__(self, name):
        self.name=name
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

class Parent:
    def can_sing(self):
        print("Sing a song")

class LuckyChild(Parent):
    pass

class UnLuckyChild:
    pass

class LuckyChild2(Parent):
    def can_dance(self):
        print("Shuffle Dance")

        

