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


def is_ingredients_sufficiants(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry. There is not enough {item}")
            return False
    return True


def total_cash():
    quarters = int(input("How many quarters?: "))
    # quarters = $0.25
    dimes = int(input("how many dimes?: "))
    # dimes = $0.10
    nickels = int(input("how many nickels?: "))
    # nickels = $0.05
    pennies = int(input("how many pennies?: "))
    # pennies = $0.01
    total_cost = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels)+(0.01 * pennies)
    return total_cost


def is_transaction_successfull(total , cost):
    if total < cost:
        print("Sorry that's not enough money. Money refunded.​")
        return False
    else:
        change = round(total -cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True


def deduct_resources(ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    



on = True

while on:
    coffee_type = input("   What would you like? (espresso/latte/cappuccino):")
    if coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif coffee_type =="off":
        on = False
    
    else:
        drink = MENU[coffee_type]
        if is_ingredients_sufficiants(drink["ingredients"]):
            total = total_cash()
            if is_transaction_successfull(total , drink["cost"]):
                deduct_resources(drink["ingredients"])
                print(f"Here is your{coffee_type} ☕️ . Enjoy!")
                profit += drink["cost"]

