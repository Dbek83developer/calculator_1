# Calculator
# add
def add(a, b):
    return a + b


# subtract
def subtract(a, b):
    return a - b


# multiply
def multiply(a, b):
    return a * b


# divide
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Cannot divide by zero")
        return None


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation = input("Enter operation: ")
        num2 = float(input("Enter second number: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        choose = input(f"Type 'y' to continue calculating with {answer} and 'n' if you want to new calculation. Any "
                       f"other for exit:")
        if choose == 'y':
            num1 = answer
        elif choose == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()
