names = []
saying = 'Adieu, adieu, to'
    
while True:
    try:
        names.append(input('Name: ') + ', ')

    except EOFError:
        if len(names) == 1:
            print (f"\n{saying} {names[0][:-2]}" )
            break

        names[-1] = 'and ' + names[-1][:-2]
        print('\n' + saying, ''.join(names))
        break
