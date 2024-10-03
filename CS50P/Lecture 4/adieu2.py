names = []

if __name__ == "__main__":
    inp = input("name: ") 
    while inp != "":
        names.append(inp)
        inp = input("name: ")

    
    s = "Adieu, adieu, to "

    size = len(names)
    match size:
        case 0:
            print("give at least one name")
            exit()
        case 1:
            s += names[0]
        case 2:
            s += names[0] + " and " + names[1]
        case _:
            count = size
            while count > 1:
                s += str(names[size - count ]) + ", "
                count -= 1 
            s += "and " + names[-1]

    print(s)
