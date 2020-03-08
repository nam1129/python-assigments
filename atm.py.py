
correct_pin = 1628
print(" ATM CASH ")
pin = int(input("Please enter your 4 digit pin:"))
tries = 3
balance=2000
withdrawals = 1

while correct_pin == 1628:
    if tries < 3 and pin!= correct_pin:
        tries+=1
        pin=int(input("Wrong pin, Enter pin again:"))
        if tries == 3 and pin!= correct_pin:
            print("ATM Card Blocked, please contact your branch for assistance!")
            
    else:
        if pin == correct_pin and tries < 4:
            print("Welcome to Express Bank")
            print("You have $20000 in your account")
            if pin == correct_pin and withdrawals < 3:
                withdrawals+=1
                cash=int(input("Please enter amount to withdraw:"))
                print("Please take your cash")
                print("Your balance is ${}".format(balance-cash))
                print("Thank you for banking with us")
            else:
                print("Withdrawal limit exceeded")
               # if balance >= 20000:
                #    print("You cannot withdraw more than the available amount")
                
                correct_pin = False
    


    

