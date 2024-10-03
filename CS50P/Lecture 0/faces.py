def convert(user_input):
    smile_replace = user_input.replace(":)", "🙂")
    frown_replace = smile_replace.replace(":(", "🙁")
    return frown_replace


def main():
    user_input = input("Please type your emoticons   ")
    print(convert(user_input))
    
main()
