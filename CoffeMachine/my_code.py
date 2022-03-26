from menu import MENU
from menu import resources


def report(remains_resources_element):
    """Report have many resources we have in our storage"""
    print(f"Water: {remains_resources_element['water']}ml")
    print(f"Milk: {remains_resources_element['milk']}ml")
    print(f"Coffee: {remains_resources_element['coffee']}g")
    print(f"Money: ${remains_resources_element['money']}")


def all_coins(user_choice_element):
    """Calculate all money from user"""
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many pennies?: ")) * 0.01
    money_all_coins = round((quarters + dimes + nickles + pennies), 2)
    return money_all_coins


def add_coins(user_choice_element, money_all_coins):
    """Calculate a change"""
    order_price = MENU[user_choice_element]['cost']
    change = money_all_coins - order_price
    return change


def calculate_money(user_choice_element):
    """Calculate how much money we should add in the cashier"""
    money_element = 0
    money_element += MENU[user_choice_element]['cost']
    return money_element


def resources_calculate(user_choice_element, remains_resources_element):
    """Calculate how many resources we should subtract from our storage"""
    water = remains_resources_element['water'] - MENU[user_choice_element]['ingredients']['water']
    milk = remains_resources_element['milk'] - MENU[user_choice_element]['ingredients']['milk']
    coffee = remains_resources_element['coffee'] - MENU[user_choice_element]['ingredients']['coffee']
    remaining_resources = {
        "water": water,
        "milk": milk,
        "coffee": coffee
    }
    return remaining_resources


money = 0
remains_resources = resources
should_continue = True

while should_continue:
    while should_continue:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == 'report':
            report(remains_resources)
            break
        # Check if we have resources
        if user_choice != 'off' and user_choice != 'report':
            if remains_resources['water'] < MENU[user_choice]['ingredients']['water']:
                print("Sorry there is not enough water.")
                break
            if remains_resources['water'] < MENU[user_choice]['ingredients']['milk']:
                print("Sorry there is not enough milk.")
                break
            if remains_resources['water'] < MENU[user_choice]['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
                break

            while should_continue:
                print("Please insert coins.")

                # Check if amount of coins which user insert greater than cost of product
                sum_of_all_coins = all_coins(user_choice)
                if sum_of_all_coins < MENU[user_choice]['cost']:
                    print("Sorry that's not enough money. Money refunded.")
                    break

                # Counting the change that we should give to user
                change = add_coins(user_choice, sum_of_all_coins)
                # Subtracting resources from our storage which equal to user order
                remains_resources = resources_calculate(user_choice, remains_resources)
                # Add money to our storage which equal to user order
                money += calculate_money(user_choice)
                # Changing amount of money in dictionary which contains data about our resources
                remains_resources['money'] = money

                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
                break
        else:
            should_continue = False
