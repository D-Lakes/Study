amount_due = 50

while 0 < amount_due <= 50:
    print(f'Amount Due: {amount_due}')
    coin = int(input('Insert Coin: '))
    match coin:
        case 25:
            amount_due -= 25
            continue
        case 10: 
            amount_due -= 10
            continue
        case 5:
            amount_due -= 5
            continue
        case _:
            continue
print(f'Change Due: {abs(amount_due)}')


