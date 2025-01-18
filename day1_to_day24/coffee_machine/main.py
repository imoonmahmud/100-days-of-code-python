from menu import MENU, resources
profit = 0 

def report(money):
    return print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")

def is_enough_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"SOrry there is not enough {item}")
            return False
    return True

def process_coins():
    coin_value = {
        'quarters': .25,
        'dimes': .10,
        'nickles': .05,
        'pennies': .01,
    }
    user_coins = {}
    for coin in coin_value:
        value = int(input(f"how many {coin}? "))
        user_coins[coin] = value
    
    user_amount = 0
    for user_coin, how_many in user_coins.items():
        for coin, value in coin_value.items():
            if user_coin == coin:
                user_amount += how_many * value

    return user_amount
    
def is_transaction_successful(user_money, drink_cost):
    global profit
    change = round(user_money - drink_cost)
    if user_money >= drink_cost:
        profit += drink_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("SOrry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

while True:
    choice = input("What you would like? (espresso/latte/cappuccino): ").lower()
    match choice:
        case 'report':
            report(profit)
        case 'off':
            break
        case _:
            drink = MENU[choice]
            if is_enough_resource(drink['ingredients']):
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])




