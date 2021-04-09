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

turn = True
profit =0


def is_resource_sufficient(order_ingredients):
    """return ingridient avialnble or not (true/false)"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item] :
            print (f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return total count of coins"""
    print("please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    # total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    print(f"total amount paid: {total}")
    return total


def is_transaction_successful(money_received, drink_cost):
    """return true when payment accepted false when reject"""
    if money_received >= drink_cost:
        change =  round(money_received-drink_cost,2)
        print(f"here the change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ordered_ingradient):
    for item in ordered_ingradient:
        resources[item] -= ordered_ingradient[item]
    print(f"enjoy your drink {drink_name}")


while turn:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        turn = False
    elif choice == "report":
        print(f" water: {resources['water']}\n milk: {resources['milk']} \n Coffee: {resources['coffee']} \n money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice, drink['ingredients'])
