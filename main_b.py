from os import *
from menu import *
from ordered import *
from time import *

menu()
print("\t\t\t\t\t\t\t\tTake your time to view our menu")
make = int(input("\t\t\t\t\t\tTo oder input 1 to exit 0: "))
if make == 1:
    sleep(3)
    if name == 'nt':
        system('cls')
        print('''\t\t\t\t\t\tEnter your order with the following code
                        Breakfast - Br
                        Lunch - Lr
                        Dinner - Di
                        Specials - Sp''')
# set the constraint to a specific number of value for specials and zero for the others
        orders()
    else:
        system('clear')
        print('''\t\t\t\t\t\tEnter your order with the following code
                        Breakfast - Br
                        Lunch - Lr
                        Dinner - Di
                        Specials - Sp''')
# set the constraint to a specific number of value for specials and zero for the others
        orders()
else:
    print("\t\t\t\t\t\tThank you for checking out our place")
    quit()
        
    