import os, platform
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator(n1, n2, operation):
    result = 0
    match operation:
        case '+':
            result += add(n1, n2)
        case '-':
            result += sub(n1, n2)
        case '*':
            result += multi(n1, n2)
        case '/':
            result += div(n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    return result

def take_input(keys):
    n1 = float(input("What's your first number?: "))
    for key in keys:
        print(key)
    operation = input("Pick an operation: ")
    n2 = float(input("What's your next number?: "))
    return n1, n2, operation


keys = ["+", "-", "*", "/"]
while True:
    n1 = float(input("What's your first number?: "))
    for key in keys:
        print(key)
    operation = input("Pick an operation: ")
    n2 = float(input("What's your next number?: "))
    result = calculator(n1, n2, operation)
    should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if should_continue not in ['y', 'n']:
        break
    while True:
        if should_continue == 'y':
            n1 = result
            for key in keys:
                print(key)
            operation = input("Pick an operation: ")
            n2 = float(input("What's your next number?: "))
            result = calculator(n1, n2, operation)
            should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
            continue
        else:
            clear()
            break