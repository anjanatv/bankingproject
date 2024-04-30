"""Write a python program to replicate a Banking system. The following features are mandatory:
1. Account login
2.Amount Depositing
3.Amount Withdrawal
Other than the above features you can add any other also."""

class bank_accnt():
    def __init__(self):
        self.accounts={}
        self.username=""
        self.password=""

    def accnt_create (self,accnt_holder, accnt_number,balance):
        self.username=input("enter username:")
        self.password=input("enter password:")
        if not self.login():
            return "username or password incorrect, try again"

        if accnt_number in self.accounts:
            return "Account exist"
        if balance<=0:
            return "balance must be above 500"

        self.accounts[accnt_number]={
            'account holder name':accnt_holder,
            'balance':balance
        }
        return "account created"


    def deposit(self,amount):
        self.accounts[accnt_number]['balance']+=amount
        #self.balance+=amount
        return "DEAR CUSTOMER, amount credited to your account"
        print(f"new balance is {self.balance}")
    def withdrawal(self,withdraw_amt):
        if (self.balance-withdraw_amt>=0):
            return "insufficient balance"
        else:
            print(f"amount{withdraw_amt} withdrawn successfully")
    def balance_check(self,accnt_number):
        if accnt_number not in self.accounts:
            return "account not exist"
        else:
            return "Your savings account balance is:",self.balance_check


a=bank_accnt()
print("1. Create account, \n 2. Deposit, \n 3. Withdraw, \n 4. Balance check, \n 5. Exit")

while True:

    selection=input("select choice from the above:")
    if selection=='1':
        accnt_number=input("enter account no.:")
        accnt_holder=input("enter account holder name:")
        balance=float(input("enter balance amount:"))
        success=bank_accnt.accnt_create(accnt_holder,balance,accnt_number)
        print(success)

    elif selection=='2':
        accnt_number=input("enter accnt number:")
        amount=float(input("enter deposit amount:"))
        succes=bank_accnt.deposit(accnt_number,amount,amount)
        print(succes)
    elif (selection=='3'):
        accnt_number = input("enter accnt number:")
        amount = float(input("enter withdraw amount:"))
        success=bank_accnt.withdrawal(accnt_number,amount,balance)
        print(success)
    elif (selection=='4'):
        accnt_number = input("enter accnt number:")
        success=bank_accnt.balance_check(accnt_number)
        print(success)
    else:
        print("exiting the pgm")















'''res=input("do you have savings account in this bank (yes/no):")
if res=="yes":
    print("continue to login")
    username=input("enter username:")
    if len(username)<6 or len(username)>10:
        print("username should have 6 characters and a maximum of 10")

    else:
        print("try again")
else:
    print("create an account")'''

'''class Bank:

    def __init__(self, amount=0.00):
        self.balance=amount
    def accnt_login(self, ):'''
'''class Bank_accnt:
    name="username"
    mobile="mobile no."
    def display(self):
        print("printing all the details")

a=Bank_accnt()
print(Bank_accnt.name,Bank_accnt.mobile)'''



'''username=input("enter username:")
password=input("enter password:")


if res==yes:
    print("enter your username ang password:")
else:
    print("create bank account")

class bank_account:
    username=
    def bank_account(username, password):


if qstn==0:
    print("enter your userid and password")
else:
    print("create account")'''

"""string = "today is 2023-04-11"
    pattern = "(\d{4})-(\d{2})-(\d{2})"
    match = re.search(pattern, string)

    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        print(f"year:{year},month:{month},day:{day}")
    else:
        print("match not found")"""