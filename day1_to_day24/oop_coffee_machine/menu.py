class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }

    
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem('latte', 200, 150, 24, 2.5),
            MenuItem('espresso', 50, 0, 18, 1.5),
            MenuItem('cappuccino', 250, 50, 24, 3),
        ]

    def get_items(self):
        options = ''
        i = 0
        for item in self.menu:
            if i == 2:
                options += f'{item.name}'
            else:
                options += f'{item.name}/'
            i += 1
        return options
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("SOrry that item is not available.")