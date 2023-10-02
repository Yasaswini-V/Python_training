def withdraw_Savings(acc,amount):
    if acc._balance-amount>5000:
        acc._balance-=amount
        return acc._balance
    else:
        return False

def withdraw_Currrent(acc,amount):
    if amount<=acc._balance:
        acc._balance-=amount
        return acc.balance
    else:
        return False

def withdraw_Overdraft(acc,amount,his_balance):
    od_limit=his_balance*(0.1)
    od=amount-acc._balance
    od_fee=od*(0.01)
    if amount <=(acc._balance+od_limit):
        acc._balance-=amount
        acc._balance-=od_fee 
        return acc._balance
    else:
        return False
class Account():
    def deposit(self,acc1,amount):
        if isinstance(acc1,Account) and amount>0:
            acc1._balance+=amount
        return acc1._balance

    def withdraw(self,acc1,amount,his_balance=0):
        if isinstance(acc1,Account) and amount>0 :
            if acc1._type=="Savings":
                bal=withdraw_Savings(acc1,amount)
                return bal
            elif acc1._type=="Current":
                bal=withdraw_Currrent(acc1,amount)
                return bal
            elif acc1._type=="Overdraft":
                bal=withdraw_Overdraft(acc1,amount,his_balance)
                return bal
            else:
                return False

class Bank():
    def open_account(self,acc_type,acc_name,acc_no,acc_pass,balance):
        acc=Account()
        acc._type=acc_type
        acc._acc_name=acc_name
        acc._acc_no=int(acc_no)
        acc._acc_pass=acc_pass
        acc._balance=int(balance)
        return acc

    def deposit(self,acc1,amount):
        return Account.deposit(self,acc1,amount)

    def withdraw(self,acc1,amount,his_balance=0):
        bal=Account.withdraw(self,acc1,amount,his_balance)
        return bal

    def transaction(self,from_acc,to_acc,amount,pwd):
        try:
            if(amount<=from_acc._balance and from_acc._acc_pass==pwd):
                from_acc._balance-=amount
                to_acc._balance+=amount
                return True
            else:
                return False
        except Exception as ex:
            print(f'The program is interrupted due to exception {ex}')

    def credit_interest(self,acc1,no_months):
        try:
            if(acc1._type=='Savings' or acc1._type=='Overdraft' and acc1._balance>0 and no_months>0):
                for i in range(no_months):
                    c_interest=acc1._balance+(acc1._balance*3.5/1200)
                    return c_interest
            else:
                return False
        except Exception as ex:
            print(f"The program is interrupted due to error {ex}")
        
class ATM(Account,Bank):
    def print_info(self,acc):
        print("-----------info-----------")
        print(f'Account type: {acc._type}')
        print(f'Account holder name: {acc._acc_name}')
        print(f'Account number: {acc._acc_no}')
        print(f'Available balance: {acc._balance}')
    try:
        def option_input(self,acc1,acc2):
            
            try:
                option=int(input("Enter the required option 1.Deposit 2.Withdraw 3.Transaction 4.Credit interest: "))
                if option==1:
                    try:
                        amount=int(input("Enter the amount to be: "))
                        Bank.deposit(self,acc1,amount)
                        self.print_info(acc1)
                    except Exception as ex:
                        print(f'The program is interrupted because of {ex}')
                elif option==2:
                    if acc1._type=='Overdraft':
                        amount=int(input("Enter the amount to be: "))
                        his_balance=int(input("Enter the historic max balance: "))
                        acc1._balance=Bank.withdraw(self,acc1,amount,his_balance)
                        self.print_info(acc1) if acc1._balance else print("The entered amount is more than the balance available or account type does not exist")
                    else:
                        amount=int(input("Enter the amount to be: "))
                        acc1._balance=Bank.withdraw(self,acc1,amount)
                        self.print_info(acc1) if acc1._balance else print("The entered amount is more than the balance available or account type does not exist")
                elif option==3:
                    amount=int(input("Enter the amount to be: "))
                    pwd=input("Enter the password again for transaction: ")
                    Trans=Bank.transaction(self,acc1,acc2,amount,pwd)
                    print(f'Amount {amount} transferred from {acc1._acc_name} to {acc2._acc_name}') if Trans else print(f'Transaction unsuccessful, Please check the password and the bank balance')
                    self.print_info(acc1) 
                    self.print_info(acc2) 
                elif option==4:
                    no_months=int(input("Enter the number of months interst to be calculated: "))
                    credit=Bank.credit_interest(self,acc1,no_months)
                    print(f'The credit interest for {months} is {credit}') if credit else print("Invalid balance or number of months entered")
                    self.print_info(acc1)
                else:
                    print("Invalid option entered")
            except Exception as ex:
                print(f"The program is interrupted because of {ex}")
    except Exception as ex:
        print(f"The program is interrupted because of {ex}")
           
icici=Bank()
acc1=icici.open_account('Overdraft','Yasaswini',1234,'Yassu@123',20000)
acc3=icici.open_account('Savings','Aaku',1377,'Aaku@123',5000)
acc4=icici.open_account('Current','Madhu',1122,'Madhu@123',25000)
acc2=icici.open_account('Savings','Rama',5678,'Rama@123',30000)
ATM().option_input(acc1,acc2)