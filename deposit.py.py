print('Welcome to the Deposit & Withdrawal Machine by Cuebic')
print('Enter correct username and pin to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter Pin:')
    if password=='2891' and username=='ato':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 3


class Bank_Account: 

    def __init__(self): 

        self.balance=100

        print("Welcome to the Deposit & Withdrawal Machine by Cuebic")
    

    def deposit(self): 

        amount=float(input("Enter amount to be Deposited: ")) 

        self.balance += amount 

        print("\n Amount Deposited:",amount) 

    def withdraw(self): 

        amount = float(input("Enter amount to be Withdrawn: ")) 

        if self.balance>=amount: 

            self.balance-=amount 

            print("\n You Withdrew:", amount) 

        else: 

            print("\n Insufficient balance  ") 

    def display(self): 

        print("\n Net Available Balance = ",self.balance) 

  


   
# creating an object of class 

s = Bank_Account() 

   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display()

