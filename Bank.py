from Account import *
class Bank():
    def deposit(self,acc,amount):
        return Account.deposit(self,acc,amount)

    def withdraw(self,bal,amount,his_balance=0):
        bal=Account.withdraw(self,bal,amount,his_balance)
        print(bal)
        return bal

    def transaction(self,from_acc,to_acc,amount,pwd):
        print(from_acc.balance)
        try:
            if(amount<=from_acc.balance and from_acc.acc_pass==pwd):
                from_acc.balance-=amount
                to_acc.balance+=amount
                return True
            else:
                return False
        except Exception as ex:
            print(f'The program is interrupted due to exception {ex}')

    def credit_interest(self,acc1,no_months):
        try:
            if( isinstance(acc1,Savings) or isinstance(acc1,Overdraft) and acc1.balance>0 and no_months>0):
                print("true")
                for i in range(no_months):
                    c_interest=acc1.balance+((acc1.balance*3.5)/100)
                    return c_interest
            elif isinstance(self,Current):
                print(f"The accont type {type(acc)} has no inetrest")
            else:
                return False
        except Exception as ex:
            print(f"The program is interrupted due to error {ex}")


        