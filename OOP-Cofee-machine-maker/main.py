from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine  = MoneyMachine()
data = Menu()
coffee_maker = CoffeeMaker()

on = True

while on:
    coffee_choice = input(f"What would you like? ({data.get_items()}): ")
    if coffee_choice == "off":
        on =False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = data.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        