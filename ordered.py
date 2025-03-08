from menu import *
from receipt_main import *


def orders():
    order = input("\t\t\t\t\t\tI would woould would love a meal from:::")
    breakfast, lunch, Dinner = 'Br', 'Lr', 'Di'
    if breakfast == order:
        print("\t\t\t\t\t\tSeems Someone is still in the morning")
        print("\t\t\t\t\t\tCheck out our breakfast menu")
        breakfast_menu()
        ordering(order)
    elif lunch == order:
        print("\t\t\t\t\t\tWe in the mood for lunch")
        print("\t\t\t\t\t\tWe are Serving")
        lunch_menu()
        ordering(order)
    elif Dinner == order:
        print("\t\t\t\t\t\tLate Night Dishes, Nice")
        print("\t\t\t\t\t\tTonight we serve")
        dinner_menu()
        ordering(order)
    else:
        print("\t\t\t\t\t\tTry again")
        # using recursion to run the code again and again until the user gets it correct
        orders()
