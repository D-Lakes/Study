import random

def generate_integers(n: int) -> tuple:
    x0 = str(random.randint(1, 9))
    x1 = str(random.randint(0, 9))
    x2 = str(random.randint(0, 9))

    y0 = str(random.randint(1, 9))
    y1 = str(random.randint(0, 9))
    y2 = str(random.randint(0, 9))

    match n:
        case 1:
            return (x0, y0)
        case 2:
            return (x0+x1, y0+y1)
        case 3:
            return (x0+x1+x2, y0+y1+y2)
    return (0, 0)


def get_level():
    while True:
        level = input('Level: ')

        try:
            level = int(level)

        except ValueError:
            continue

        valid_levels = [1, 2, 3]

        if level not in valid_levels:
            continue
        else:
            return level

def main():
    idx = 0
    score = 0
    level = get_level()

    while idx < 10:
        x, y = generate_integers(level)
        answer = int(x) + int(y)
        idx +=1 

        for attempt in [1, 2, 3, 4]:
            if attempt == 4:
                print(f"{x} + {y} = {answer}")
                break

            guess = input(f'{x} + {y} = ')

            try:
                if int(guess) == answer:
                    print('Correct!')
                    score += 1
                    break
                else:
                    print('EEE')
            except ValueError:
                print('EEE')

    print(f"Score: {score}")





if __name__ == "__main__":
    main()

