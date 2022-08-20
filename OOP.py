'''class Calculator:
    def sum(slef,a,b):
        return a+b
    def mul(self,a,b):
        return a*b
    def pow(self,a,b):
        return a**b
sc=Calculator()
sc.sum(2,3)
class SCiCalculator(Calculator):
    def div(slef,a,b):
        return a/b
sc1=SCiCalculator()
print(sc1.pow(2,2))
print(SCiCalculator.mro())      
    '''

'''from re import U


class User:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def showDitails (self):
        print(f'name: {self.name}')
        print(f'age:{self.age}')
        print(f'gender :{self.gender}')

    
class Bank(User):
    
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    
    def deposite(self,amount):
        self.balance+=amount
        print(f'Currnent Balance :{self.balance}')
    
    def withdraw(self,amount):
        if amount>self.balance:
            print(f'insuffcient balance :{self.balance}')
            return
        self.balance-=amount
        print(f'Currnent Balance :{self.balance}')
    
    def showBalance(self):
        self.showDitails()
        print(f'Balance :{self.balance}')
        


u1=Bank('ziad',20,'male')
#u1.showDitails()
u1.deposite(1000)
u1.withdraw(2000)
u1.showBalance()'''
#! import helloWorld as hw