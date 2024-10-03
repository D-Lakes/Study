from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

try:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            user_input = input('Input: ')
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(user_input))
        else:
            sys.exit('Font not found')
    else:
        sys.exit('use correct flag')
except IndexError:
    figlet.setFont(font=figlet.getFonts()[random.randint(0, 550)])
    print(f"Output:\n\n{figlet.renderText(user_input)}")
