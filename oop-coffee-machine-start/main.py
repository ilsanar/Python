from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu=Menu()
coffe_machine=CoffeeMaker()
my_money_machine = MoneyMachine()


on=True
while on:
    options=my_menu.get_items()
    choice = input(f"What would you like? {options}:").lower()

    if choice =="off":
        on=False
    elif choice=="report":
        coffe_machine.report()
        my_money_machine.report()
    else:
        order = my_menu.find_drink(choice)
        if order and coffe_machine.is_resource_sufficient(order) and my_money_machine.make_payment(order.cost):
            coffe_machine.make_coffee(order)
