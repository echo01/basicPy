# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
receive_money = 0



# TODO: 1. Print report of all coffee machine resources
def report_machine():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {profit}$")


# TODO: 2. Check resources sufficient to make drink order.
def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 3. Process coins
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO: 4. Check transaction successful?
def is_transaction_successful(order_cost):
    global profit
    if receive_money > order_cost:
        profit += order["cost"]
        change = receive_money - order["cost"]
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 5. Make Coffee.
def make_coffee(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_machine_run=True

while is_machine_run:
    cmd = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if cmd == "exit":
        print("Thank you good bye.")
        is_machine_run = False
    elif cmd == "report":
        report_machine()
    elif cmd == "espresso" or cmd == "latte" or cmd == "cappuccino":
        drink_name = cmd
        order = MENU[drink_name]
        if is_resource_enough(order["ingredients"]):
            receive_money = process_coins()
            print(f"receive money: {receive_money}")
            if is_transaction_successful(order["cost"]):
                make_coffee(drink_name, order["ingredients"])
    else:
        print("Invalid command try again.")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
