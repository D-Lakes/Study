




def check_fuel_gauge():
    while one_func() == None: # Change Here
        one_func()


def one_func():

    try:
        (x,y) = input('Fraction: ').split(sep='/')
        if x > y:
            print('Please enter a proper fraction')
            return None
        decimal = (int(x)/int(y) * 100) # The blah variable name was triggering

        if 1 < decimal < 99:
            print(f'{decimal:.0f}%')
        elif decimal <= 1:
            print('E')
        elif decimal >= 99:
            print('F')
        return True # Add This

    except ValueError:
        print('Please enter a natural number')
        return None
    except ZeroDivisionError:
        print("Don't divide by 0...trust me")
        return None







if __name__ == '__main__':
    check_fuel_gauge()
