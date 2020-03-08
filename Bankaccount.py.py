import random

Accounts=[]
def createAccount():
    details={"AccountId":"","pin":"","balance":0}
    details['AccountId']=random.randint(99,999)
    details['pin']=input("enter your desired pin: ")
    Accounts.append(details)
    return getAccount(details['AccountId'],details['pin'])

def getAccount(AccountId,pin):
    for item in Accounts:
        if item.get("AccountId") == AccountId and item.get('pin') == pin:
            return Accounts.index(item)

def deposit(index):
    Accounts[index]['balance']+=float(input('Deposit\nenter deposit amount: '))

def withdrawal(index):
    amt = float(input('enter withdraw amount: '))
    if amt <= Accounts[index]['balance']:
        Accounts[index]['balance']-=amt
    else:
        print('you cannot withdraw more than your current balance, Ghc{}'.format(Accounts[index]['balance']))

def sessionControl(index):
    print(index)
    keepAlive=True
    while(keepAlive):
        opt = input('Welcome,\nselect 1 to end session\nselect 2 to make a withdrawal\nselect 3 to view account details\nselect 4 to make a deposit\n')
        if opt =='1':
            deposit(index)
        elif opt =='2':
            withdrawal(index)
        elif opt =='3':
            print(Accounts[index]) 
        elif opt =='4':
            keepAlive = False
        else:
            print('enter a valid number')

def main():
    keepAlive=True
    while(keepAlive):
        opt = input('Hello,\nselect 1 to log into your account\nselect 2 to create new account\nselect 3 to end session\n')
        if opt =='1':
            AccountId=int(input('enter your account number: '))
            pin=input('enter your account pin: ')
            sessionControl(getAccount(AccountId,pin))
        elif opt =='2':
            sessionControl(createAccount())
        elif opt =='3':
            keepAlive = False
        else:
            print('enter a valid number')
    
if __name__ == "__main__":
    main()
