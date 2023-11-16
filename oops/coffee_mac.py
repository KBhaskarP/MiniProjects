menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(menu,choice,resources):
    items=menu[choice]["ingredients"]
    for keys in items.keys():
        if items[keys]>resources[keys]:
            print(f"Sorry! There is not enough {keys}")
            return False
        else:
            resources.update({keys:resources[keys]-items[keys]})
    return True
            
def payment():
    quarters=int(input("Enter number of quarters: "))
    dimes=int(input("Enter number of dimes: "))
    nickles=int(input("Enter number of nickles: "))
    penny=int(input("Enter number of pennies: "))
    recieved_amt=0.25*quarters+0.10*dimes+0.05*nickles+0.01*penny
    return recieved_amt
    
power=True
moeny_in_the_machine=0
while power:
    choice=input("What would you like? (espresso/latte/cappuccino/report): ")
    if choice=="report":
        print(resources,moeny_in_the_machine)
    elif choice=="espresso":
        # print(resources)
        bill=menu[choice]["cost"]
        available=check_resources(menu,choice,resources)
        if available is True:
            print(f"Your bill is ${bill}")
            amount_recieved=payment()
            if amount_recieved<bill:
                print(f"Sorry that's not enough money. Money refunded. collect your ${amount_recieved}")
            elif amount_recieved>bill:
                change_amount=int(round(amount_recieved-amount_recieved,2))
                print(f"Here is ${change_amount} in change.")
                print(f"Enjoy your {choice}")
                moeny_in_the_machine+=bill
        # print(resources)
    elif choice=="cappuccino":
        bill=menu[choice]["cost"]
        available=check_resources(menu,choice,resources)
        if available is True:
            print(f"Your bill is ${bill}")
            amount_recieved=payment()
            if amount_recieved<bill:
                print(f"Sorry that's not enough money. Money refunded. collect your ${amount_recieved}")
            elif amount_recieved>bill:
                change_amount=int(round(amount_recieved-amount_recieved,2))
                print(f"Here is ${change_amount} in change.")
                print(f"Enjoy your {choice}")
                moeny_in_the_machine+=bill
    elif choice=="latte":
        bill=menu[choice]["cost"]
        available=check_resources(menu,choice,resources)
        if available is True:
            print(f"Your bill is ${bill}")
            amount_recieved=payment()
            if amount_recieved<bill:
                print(f"Sorry that's not enough money. Money refunded. collect your ${amount_recieved}")
            elif amount_recieved>bill:
                change_amount=int(round(amount_recieved-amount_recieved,2))
                print(f"Here is ${change_amount} in change.")
                print(f"Enjoy your {choice}")
                moeny_in_the_machine+=bill
    else:
        power=False
