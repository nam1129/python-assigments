
def charges():
    units=int(input("Enter the unit here: "))    
    charge=0

    if units>0 and units<=120:
        charge=units*5.45
        print('Your charge is {}'.format(charge))

    elif units>120 and units<=240:
        charge=654+(units-120)*6.7
        print('Your charge is {}'.format(charge))
    else:
        charge=654+804+(units-240)*7.7
        print('Your charge is {}'.format(charge))



def quantity_consumed():
    units=int(input("Enter the unit here: "))    
    hour=int(input("Enter an hour between 1 to 24"))
    if hour>0 and hour<=24:
        kilowatt_per_hour= units*hour
        print('The quantity consumed is {}'.format(kilowatt_per_hour))

    else:
        print('The hour you entered is invalid')



print(charges())
print(quantity_consumed())
        
