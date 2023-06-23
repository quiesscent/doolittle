from os import *
from time import *


def rec_pri(items, item):
    amount = []
    items_br_pr = {'Br24': 20, 'Br46': 50, 'Br54': 100, 'Br78': 70, 'Br56': 80, 'Br34': 140, 'Br89': 115, 'Br21': 200,
                   'Br12': 90}

    items_lu_pr = {'Lr50': 2000, 'Lr15': 500, 'Lr30': 1000, 'Lr55': 900, 'Lr70': 700, 'Lr40': 2500, 'Lr65': 2000,
                   'Lr45': 1200, 'Lr05': 200}

    items_di_pr = {'Di08': 60, 'Di04': 200, 'Di07': 1200, 'Di03': 2000, 'Di10': 200, 'Di21': 500, 'Di19': 900,
                   'Di12': 1500, 'Di88': 2500}

    print("\t\t\t\t\t\t\tThank you for choosing us here is your receipt")
    print("\t\t\t\t---------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tDOOLITTLE VCAFE")
    print("\t\t\t\t---------------------------------------------------------------------")
    print("\t\t\t\tCode\t\t\t\tQuantity\t\t\tPrice")
    print("\t\t\t\t---------------------------------------------------------------------")

    for item in items:
        if item in items_br_pr:
            num = items[item]
            num = int(num)
            print(f"\t\t\t\t{item} \t\t\t\t {items[item]} \t\t\t\t {items_br_pr[item] * num}")
            amount.append(items_br_pr[item] * num)
        elif item in items_di_pr:
            num = items[item]
            num = int(num)
            print(f"\t\t\t\t{item} \t\t\t\t {items[item]} \t\t\t\t {items_di_pr[item] * num}")
            amount.append(items_di_pr[item] * num)
        else:
            num = items[item]
            num = int(num)
            print(f"\t\t\t\t{item} \t\t\t\t {items[item]} \t\t\t\t {items_lu_pr[item] * num}")
            amount.append(items_lu_pr[item] * num)
    print("\t\t\t\t\t\t\t\t\t\t\tTotal", sum(amount))
    quit()


def ordering(booking):
    bookings = {}
    total = []
    run = 1
    while run:
        book = input('''\t\t\t\t\t\tEnter the item you want:
                        \t\t\tIf done Y | y for reciept:: ''')
        if book != 'y' and book != 'Y':
            quantity = input("\t\t\t\t\t\tEnter the quantity::: ")
            bookings[book] = quantity

        else:
            if name == 'nt':
                system('cls')
            else:
                system('clear')
            print("\t\t\t\t\t\t\t\tGetting your order\n")
            sleep(5)
            cheker = list(bookings.keys())
            rec_pri(bookings, cheker)