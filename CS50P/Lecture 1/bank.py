user_input = input("Greeting: ")

if user_input.lower().strip().startswith('hello'):
    print('$0')
elif user_input.lower().strip().startswith('h'):
    print('$20')
else:
    print('$100')
