from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_make = CoffeeMaker()
mon_machine = MoneyMachine()
coffee_make.report()
mon_machine.report()
is_coffee = True
while is_coffee:
    choice = input(f"what would you like {menu.get_items()} ")
    if choice == "report":
        coffee_make.report()
        mon_machine.report()
    elif choice == "off":
        is_coffee = False
    else:
        drink = menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(drink):
            if mon_machine.make_payment(drink.cost):
                coffee_make.make_coffee(drink)