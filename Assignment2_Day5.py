class Account:
    pass

def create(acc_no,name,pwd,bal,i_rate):
    Acc=Account()
    Acc.acc_no=int(acc_no)
    Acc.name=name
    Acc.pwd=pwd
    Acc.balance=int(bal)
    Acc.i_rate=int(i_rate)
    return Acc

def is_valid(acc):
    return isinstance(acc,Account)

def deposit(acc,amount):
    if is_valid(acc) and amount >0:
        acc.balance+=amount
        print(f"Amount credited into {acc.name}'s account")
        print(f"Updated balance {acc.balance}")
    else:
        print("Entered amount is negative")

def withdraw(acc,amount,pwd):
    if is_valid(acc) and amount>0 and acc.balance>amount and acc.pwd==pwd:
        acc.balance-=amount
        print(f"Amount debited from {acc.name}'s account")
        print(f"Updated balance {acc.balance}")
    else:
        print("Amount requested is more than the balance or the password entered is wrong")

def credit_i(acc,no_mon):
    if is_valid(acc):
        for i in range(no_mon):
            acc.balance+=(acc.balance*acc.i_rate/1200)
        print(f"Credit for {no_mon} month is {acc.balance}")

def info(acc):
    if is_valid(acc):
        print(f"Account number = {acc.acc_no}")
        print(f"Account holder name = {acc.name}")
        print(f"Balance = {acc.balance}")
        print(f"Interest rate = {acc.i_rate}")
    else:
        print("Invalid account")

def main(acc_no,name,pwd,balance,i_r,d_amount=0,c_amount=0,no_month=0):
    acc=create(acc_no,name,pwd,balance,i_r)
    print("-----------Info---------- ")
    info(acc)
    if(d_amount>0):
        print("------------Deposit-----------------")
        deposit(acc,d_amount)
    if(c_amount>0):
        print("----------------Withdraw-------------- ")
        pwd=input("Re-enter the password: ")
        withdraw(acc,c_amount,pwd)
    if(no_month>0):
        print("------------Credit rate----------- ")
        credit_i(acc,no_month)

main(1234,'Yasaswini','Yassu@123',2500,3,200,300,1)