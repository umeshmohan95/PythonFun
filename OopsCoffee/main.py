from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0
turn = True

coffee_maker = CoffeeMaker()
menu = Menu()
options = menu.get_items()
money = MoneyMachine()




while turn:
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        turn = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink=menu.find_drink(choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink) :
            # total_amount=money.process_coins()
            money.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
