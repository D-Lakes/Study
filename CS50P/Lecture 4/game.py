import random

while True:
    level = input('Level: ')

    try:
        level = int(level)

    except ValueError:
        continue

    if level > 0:
        break

number = random.randint(1, level)
guess = str()

while guess != number:
    guess = input('Guess: ')

    try:
        guess = int(guess)
        if not guess  > 0: 
            continue

    except ValueError:
        continue

    if guess < number:
        print('too small')
    elif guess > number:
        print('too large')
    elif guess == number:
        print('Correct')
