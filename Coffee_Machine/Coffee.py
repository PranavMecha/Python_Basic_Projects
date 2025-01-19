MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

def paye():
    print("Please insert Coins :")
    quarters = float(input("How many quarters? :"))
    dimes = float(input("How many dimes? :"))
    nickels = float(input("How many nickels? :"))
    pennies = float(input("How many pennies? :"))
    pay=(0.01*pennies)+(0.10*dimes)+(0.25*quarters)+(0.05*nickels)
    return pay

def machine(bevrage):
    global profit
    if bevrage=="cappuccino" or bevrage=="latte" or bevrage=="espresso":

        req_water = MENU[bevrage]["ingredients"]["water"]

        req_milk = MENU[bevrage]["ingredients"]["milk"]

        req_coffee = MENU[bevrage]["ingredients"]["coffee"]

        money = MENU[bevrage]["cost"]
        if resources["water"]>req_water and resources["milk"] - req_milk and resources["coffee"] - req_coffee:
            resources["water"]=resources["water"] - req_water
            resources["milk"]=resources["milk"] - req_milk
            resources["coffee"]=resources["coffee"] - req_coffee
            payment = paye()
            if payment < money:
                print("Sorry,that's not enough money.Money Refunded")
            else:
                profit+=money
                change = payment - money
                print(f"Your change is ${change}")
        elif resources["water"]<req_water:
            print("Sorry Insufficient Water")
        elif resources["milk"]<req_milk:
            print("Sorry Insufficient Milk")
        else:
            print("Sorry Insufficient Coffee")

    elif bevrage=="report":
        print(f"""Water : {resources["water"]}
Milk : {resources["milk"]}
Coffee : {resources["coffee"]}
Money :{profit}""")
    else:
        print("Please Enter Valid Command.")

profit=0
while True:
    drink=input("What would you like ? (espresso/latte/cappuccino) :").lower()
    if drink!="off":
        machine(drink)
    else:
        print("Switching off.")
        break






