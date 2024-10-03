def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


user_input = input('Expression: ')

x, y, z = user_input.split(' ')
x = int(x)
z = float(z)

match y:
    case '+':
        print(add(x, z))
    case '-':
        print(subtract(x, z))
    case '*':
        print(multiply(x, z))
    case('/'):
        print(divide(x, z))
    case _:
        print('funky expression')


