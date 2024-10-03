def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Minimum and maximum length requirement
    if not 2 <= len(s) <= 6:
        return False
    # Only letters or numbers allowed; No periods, spaces, or punctuation marks
    if not s.isalnum():
        return False
    # First two characters must be letters
    if not s[:1].isalpha():
        return False
    # The final rules only apply to the last four characters in str
    # Per 2nd rule above last four characters are either letters or numbers
    # Letters cannot follow digits and the first digit cannot be 0
    last_four = s[1:]
    
    for i in range(len(last_four)):
        # If the character is not a digit it must be a letter so move on to next character
        if last_four[i].isdigit():
            # Checks if first digit is 0
            if last_four[i] == '0':
                return False
            # Checks rest of characters for letters
            if last_four[i:].isdigit():
                return True
            else:
                return False
        else:
            continue
    

main()

