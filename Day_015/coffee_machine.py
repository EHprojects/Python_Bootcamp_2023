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
}


def resource_report(machine_money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    # money = resources["money"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${machine_money}")


def check_resources(item):
    menu_item = MENU[item]
    for ingredient in menu_item["ingredients"]:
        if resources[ingredient] < menu_item["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        # print(menu_item["ingredients"][ingredient])
        # print(resources[ingredient])
    return True


def take_money(item):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    item_cost = MENU[item]["cost"]
    if total > item_cost:
        change = round(total - item_cost, ndigits=2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(item):
    menu_item = MENU[item]
    for ingredient in menu_item["ingredients"]:
        resources[ingredient] -= menu_item["ingredients"][ingredient]
    print(f"Here is your {item} ☕️. Enjoy!")


machine_on = True
machine_money = 0

while machine_on:

    # Prompt for a menu choice
    menu_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if menu_choice == "report":
        resource_report(machine_money)
    elif menu_choice == "off":
        machine_on = False
    else:
        if check_resources(menu_choice):
            if take_money(menu_choice):
                machine_money += MENU[menu_choice]["cost"]
                make_drink(menu_choice)
