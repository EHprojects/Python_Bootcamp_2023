from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

machine_on = True

while machine_on:

    menu_choice = input(f"What would you like? ({menu.get_items()}): ")
    if menu_choice == "off":
        machine_on = False
    elif menu_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(menu_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
