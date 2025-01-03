import menu
import money_machine
import coffee_maker
from prettytable import PrettyTable

menu = menu.Menu()
money_machine = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()
table = PrettyTable()
table.add_column('Drink', ['Latte', 'Espresso', 'Cappuccino'])
table.add_column('Price', ['$2.5', '$1.5', '$3'])

count = 0
while True:
    if count == 0:
        print(table)
    count += 1
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    match choice:
        case 'report':
            coffee_maker.report()
            money_machine.report()
        case 'off':
            break
        case _:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
