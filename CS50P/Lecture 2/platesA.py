def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #max of 6 char min of 2 
    if len(s) < 2 or len(s) > 6:
        return False

    firstNum = True
    isAlph = 0
    for i in s:
        if i.isalnum() == False:
            return False

        if i.isnumeric() and firstNum == True :
        #first 2 are letters
            if isAlph < 2:
                return False
            if i == "0":
                return False
            firstNum = False

        if i.isalpha():
        #letters cannot proceed numbers 
            if firstNum == False:
                return False
        #at least 2letters
            isAlph+=1

    return True

main()

