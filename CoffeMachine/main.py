from art import cup
MENU = {
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
    "money":0
}
#TODO 3. Print report.
def print_report():
    """Print resources in machine"""
    for i in resources:
        print(f"{i}: {resources[i]}")


#TODO 4. Check resources sufficient?
def check_resources(drink):
    """Checks if there is enough resources for customer's choice"""
    for i in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][i]>resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True
#TODO 5. Process coins

def process_coins():
    """Asks for coins and calculates amount from given coins"""
    print("Please insert coins:")
    coins={
        "quarters":{
            "amount":0,
            "multiplier":0.25
        },
        "dimes": {
            "amount": 0,
            "multiplier": 0.10
        },
        "nickles": {
            "amount": 0,
            "multiplier": 0.05
        },
        "pennies": {
            "amount": 0,
            "multiplier": 0.01
        },
    }

    amount_of_money=0.00
    for coin in coins:
        coins[coin]["amount"]=int(input(f"How many {coin}:"))
        amount_of_money+=coins[coin]["amount"]*coins[coin]["multiplier"]
    return amount_of_money
#TODO 6. Check if transaction successful

def resolve_transaction(choice,cash,turnover):
    """Takes money from customer cashes in for selected drink and returns change"""
    drink_cost=MENU[choice]["cost"]
    turnover += drink_cost
    change = round(cash-drink_cost,2)
    if change>0:
        print (f"Here is ${change} dollars in change.")
    return turnover

#TODO 7. Make coffe
def make_coffe(choice,ingredients):
    """Takes customer choice and subtracts right amount of ingredients from resources """
    for ingredient in MENU[choice]["ingredients"]:
        ingredients[ingredient]-=MENU[choice]["ingredients"][ingredient]
    print(f"Here is your {choice}. Enjoy!")


off=False
print(cup)
while not off:

    #TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    for item in MENU:
        print(f"{item}: ${MENU[item]["cost"]} ")
    selection=input("What would you like? (espresso/latte/cappuccino):").lower()
    #TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.

    if selection=="off":
        off=True

    elif selection=="report":
        print_report()
    elif MENU.get(selection):
        if check_resources(selection):
            money=process_coins()
            if money>=MENU[selection]["cost"]:
                resources["money"]=resolve_transaction(selection,money,resources["money"])
                make_coffe(selection,resources)

            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Sorry. There is no {selection} in menu. Please. Try again")




