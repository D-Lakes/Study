def check_fuel_gauge():
    while True:
        user_input = get_input()
        user_input = clean_input(user_input)

        if check_input_format(user_input) == None:
            continue
        else:
            user_input = check_input_format(user_input)

        if check_input_values(user_input) == None:
            continue
        else:
            user_input = check_input_values(user_input)

        if analyze_input(user_input) == None:
            continue
        else:
            user_input = analyze_input(user_input)

        display_fuel_gauge(user_input)
        break


def get_input():
    user_input = input('Fraction: ')
    return user_input

def clean_input(user_input):
    x, y = user_input.split(sep='/')
    return (x, y)

def check_input_format(user_input):
    try:
        return tuple(map(int, user_input))
    except ValueError:
        print('Please enter a natural number')
        return None

def check_input_values(user_input):
    x, y = user_input
    if x > y:
        print('Please enter a proper fraction')
        return None
    return (x, y)

def analyze_input(user_input):
    x, y = user_input
    try:
        return (x/y * 100)
    except ZeroDivisionError:
        print("Don't divide by 0...trust me")
        return None

def display_fuel_gauge(user_input):
    if 1 < user_input < 99:
        print(f'{user_input:.0f}%')
    elif user_input <= 1:
        print('E')
    elif user_input >= 99:
        print('F')
    

if __name__ == '__main__':
    check_fuel_gauge()
