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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(drink_ingredients):
    """Checks if there is enough ingredients in machine for selected drink."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"There isn't enough {item} to make a coffee.")
            return False
    return True

def process_coins():
    """Calculates the money customer gave it to machine."""
    quarter = int(input("how many quarters?: ")) * 0.25
    dime = int(input("how many dime?: ")) * 0.1
    nickle = int(input("how many nickles?: ")) * 0.05
    penny = int(input("how many pennies?: ")) * 0.01
    total = quarter + dime + nickle + penny
    return total

def is_transaction_successful(coin, drink):
    """Checks if customer gave enough money for drink and returns exchange."""
    global profit
    if drink["cost"] >= coin:
        print("You don't have enough money to purcase this drink.")
        return False
    else:
        exchange = round(coin - drink["cost"] , 2)
        profit += drink["cost"]
        print(f"Here is your exchange {exchange}$")
        return True        

def making_coffee(drink):
    for item in drink:
        resources[item] = resources[item] - drink[item]


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: {profit}$") # Makinanın topladığı para    
    else:
        request = MENU[choice]
        if is_resources_sufficient(request["ingredients"]):
            money_paid = int(process_coins())
            if is_transaction_successful(money_paid, request):
                making_coffee(request["ingredients"])
                print(f"Here is your {choice}, Have fun <3.")


