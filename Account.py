class Account():
    def deposit(self,acc,amount):
        if isinstance(acc,Account) and amount>0:
            acc.balance+=amount
        return acc.balance

    def withdraw(self,bal,amount,his_balance=0):
        if isinstance(self,Overdraft):
            bal=Overdraft.withdraw(self,bal,amount,his_balance)
            return bal

        elif isinstance(self,Savings):
            bal=Savings.withdraw(self,bal,amount)
            return bal

        elif isinstance(self,Current):
            bal=Current.withdraw(self,bal,amount)

class Savings(Account):
    def __init__(self,acc_name,acc_no,acc_pass,balance):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.acc_pass=acc_pass
        self.balance=balance
    
    def withdraw(self,bal,amount):
        if bal-amount>5000:
            bal-=amount
            return bal
        else:
            return False

class Current(Account):
    def __init__(self,acc_name,acc_no,acc_pass,balance):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.acc_pass=acc_pass
        self.balance=balance

    def withdraw(self,bal,amount):
        if amount<=bal:
            bal-=amount
            return bal
        else:
            return False
         
class Overdraft(Account):
    def __init__(self,acc_name,acc_no,acc_pass,balance):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.acc_pass=acc_pass
        self.balance=balance
        
    def withdraw(self,bal,amount,his_balance=0):
        if isinstance(self,Overdraft):
            od_limit=his_balance*(0.1)
            od=amount-bal
            od_fee=od*(0.01)
            if amount<=(bal+od_limit):
                bal-=amount
                bal-=od_fee 
                return bal
            else:
                return False
