# Programming Project 1: Make Change
# This program will take the input change_amount and sort it out in the most efficient way to give back
# change in the form of coin currencies such as quarters, dimes, nickels, and cents
change_amount=-1
while 0 > change_amount or 99 <  change_amount :
    try :
        change_amount=int(input("Enter amount of change (0-99): "))
        if input in range(1,10):
            break
        else:
            print("That input is not in range")
    except ValueError :
        print("That input is not an integer")
quarters=0
dimes=0
nickels=0
cents=0
if change_amount>0 :
    quarters=change_amount//25
    change_amount=change_amount%25
    if change_amount>0 :
        dimes=change_amount//10
        change_amount=change_amount%10
        if change_amount>0 :
            nickels=change_amount//5
            change_amount=change_amount%5
            if change_amount>0 :
                cents=change_amount
print("Quarters: %s \t Dimes: %s \nNickels: %s \t Cents: %s" % (quarters, dimes, nickels, cents))
