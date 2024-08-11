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

Resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "revenue": 0
}


def format_data(resource):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    money = resource["revenue"]
    return f"Water: {water} ml\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}"


def check_resources(order, resource):
    """ send argument dictionary of order use and resource"""
    check = 0
    order["need"] = ""
    order["enough"] = True
    menu = MENU[order["order"]]["ingredients"]
    order["water"] = menu["water"]
    check = resource["water"] / order["water"]
    if check < 1:
        order["need"] = "water"
        order["enough"] = False

    if "milk" in menu:
        order["milk"] = menu["milk"]
        check = resource["milk"] / order["milk"]
        if check < 1:
            order["need"] += "milk"
            order["enough"] = False
    else:
        order["milk"] = 0

    order["coffee"] = menu["coffee"]
    check = resource["coffee"] / order["coffee"]
    if check < 1:
        order["need"] += "coffee"
        order["enough"] = False
    return order


def calculate_change(receive, cost):
    return receive - cost


def make_coffee(order, resource):
    resource["water"] -= order["water"]
    resource["milk"] -= order["milk"]
    resource["coffee"] -= order["coffee"]
    return resource


# TODO: 1. Print report of all coffee machine resources
def coffee_machine(resources):
    check_menu = True
    resource_status = ""
    order_use = {
        "order": "",
        "water": 0,
        "milk": 0,
        "coffee": 0,
        "need": "",
        "enough": True
    }
    coin_inserted = {"quarters": 0,
                     "dimes": 0,
                     "nickles": 0,
                     "pennies": 0,
                     "receive": 0,
                     "change": 0
                     }
    cmd = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if cmd == "report":
        print(format_data(resources))
        check_menu = False
    elif cmd == "espresso" or cmd == "latte" or cmd == "cappuccino":
        check_menu = True
        order_use["order"] = cmd
        order_use = check_resources(order_use, resources)
    elif cmd == "exit":
        return False
    else:
        print("Invalid order.")
        check_menu = False
    # TODO: 2. Check resources sufficient to make drink order.
    if check_menu :
        if order_use["enough"]:
            print("Please insert coins.")
            # Todo: 3. Process coins
            coin_inserted["quarters"] = int(input("How many quarters?: "))
            coin_inserted["dimes"] = int(input("How many dimes?: "))
            coin_inserted["nickles"] = int(input("How many nickles?: "))
            coin_inserted["pennies"] = int(input("How many pennies?: "))
            coin_inserted["receive"] = coin_inserted["quarters"] * 0.25 + coin_inserted["dimes"] * 0.1 + coin_inserted[
                "nickles"] * 0.05 + coin_inserted["pennies"] * 0.01
            # print(Coin_Inserted)
            # Todo: 4. Check transaction successful?
            coin_inserted["change"] = calculate_change(coin_inserted["receive"], MENU[cmd]["cost"])
            if coin_inserted["change"] > 0:
                # Todo: 5. Make Coffee.
                resources["revenue"] += MENU[cmd]["cost"]
                resources = make_coffee(order_use, resources)
                print(f"resource left = {resources}")
                print(f"Here is {coin_inserted['change']} in change.")
                print(f"Here is your {order_use['order']} ☕️Enjoy!😉")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {order_use['need']}")
    return True


machine_status = True
while machine_status:
    machine_status=coffee_machine(Resources)
print("Thank you good Bye.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
