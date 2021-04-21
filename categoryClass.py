class Category:
    def __init__(self,category,amount,balance = 0):
        self.category = category
        self.amount = amount
        self.balance = balance
        
    def deposit(self,depositAmount):
        self.balance += depositAmount
        print('Deposited ${0}. Total balance after deposit is - ${1}'.format(depositAmount,self.balance))
    
    def withdraw(self,withdrawAmount):
        self.balance -= withdrawAmount
        print('withdrawed ${0}. Total balance after withdrawl is - ${1}'.format(withdrawAmount,self.balance))
        
    def transfer(self,transferAmount):
        self.balance -= transferAmount
        print('transferred amount ${0}. Total balance after transfer is - ${1}'.format(transferAmount,self.balance))
        
    def checkBalance(self):
        print('your balnce availabel is ${0}'.format(self.balance))
        
    def purchaseCategory(self):
        if(self.amount <= self.balance):
            self.balance -= self.amount
            print('your purchase of {0} is successful'.format(self.category))
            print('Post purchase your balance is ${0}'.format(self.balance))
        else:
            print('your purchase of {0} is worth ${1}. But your available balance is ${2}'.format(self.category,self.amount,self.balance))
            
        
categoryObj = Category('Car',12000,10000)
categoryObj.deposit(5000)
categoryObj.withdraw(500)
categoryObj.transfer(500)
categoryObj.checkBalance()
categoryObj.purchaseCategory()
