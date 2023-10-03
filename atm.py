from Bank import *
from Account import *
class ATM():
    def print_info(self,acc):
        print("-----------info-----------")
        print(f'Account type: {type(acc)}')
        print(f'Account holder name: {acc.acc_name}')
        print(f'Account number: {acc.acc_no}')
        print(f'Available balance: {acc.balance}')

    def open_account(self,acc_type,acc_name,acc_no,acc_pass,bal):
            if acc_type=='Savings':
                acc=Savings(acc_name,acc_no,acc_pass,bal)
                self.print_info(acc)
                return acc
            elif acc_type=='Current':
                acc=Current(acc_name,acc_no,acc_pass,bal)
                self.print_info(acc)
                return acc
            elif acc_type=='Overdraft':
                acc=Overdraft(acc_name,acc_no,acc_pass,bal)
                self.print_info(acc)
                return acc

    def option_input(self):
        while True:
            option=int(input("Enter the required option 1.open account 2.Deposit 3.Withdraw 4.Transaction 5.Credit interest 0.exit "))
            if option==1:
                acc_type=input("Enter the account type: ")
                acc_name=input("Enter the account holder name: ")
                acc_no=int(input("Enter the account number: "))
                acc_pass=input("Enter the password: ")
                bal=int(input("Enter the balance: "))
                acc=self.open_account(acc_type,acc_name,acc_no,acc_pass,bal)
            elif option==2:
                if isinstance(acc,Account):
                    amount=int(input("Enter the amount?"))
                    Bank.deposit(self,acc,amount)
                    self.print_info(acc)
            elif option==3:
                if isinstance(acc,Overdraft):
                    amount=int(input("Enter the amount to be: "))
                    his_balance=int(input("Enter the historic max balance: "))
                    acc.balance=Bank.withdraw(acc,acc.balance,amount,his_balance)
                    self.print_info(acc) if acc.balance else print("The entered amount is more than the balance available or account type does not exist")
                else:
                    amount=int(input("Enter the amount to be: "))
                    acc.balance=Bank.withdraw(acc,acc.balance,amount)
                    self.print_info(acc) if acc.balance else print("The entered amount is more than the balance available or account type does not exist")
            elif option==4:
                amount=int(input("Enter the amount to be: "))
                pwd=input("Enter the password again for transaction: ")
                acc2=self.open_account('Savings','Rama',2,'Rama@123',23000)
                Trans=Bank.transaction(self,acc,acc2,amount,pwd)
                print(f'Amount {amount} transferred from {acc.acc_name} to {acc2.acc_name}') if Trans else print(f'Transaction unsuccessful, Please check the password and the bank balance')
                self.print_info(acc) 
                self.print_info(acc2) 
            elif option==5:
                no_months=int(input("Enter the number of months interst to be calculated: "))
                credit=Bank.credit_interest(self,acc,no_months)
                print(f'The credit interest for {no_months} is {credit}') if credit else print("Invalid balance or number of months entered")
                self.print_info(acc)
            elif option==0:
                break
            else:
                print("Invalid option entered")
            
ATM().option_input()