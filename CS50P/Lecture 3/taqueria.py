menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def create_shopping_cart():
    add_item()

def add_item():
    shopping_cart = []
    while True:
        try:
            item = input('Item: ').title()
            if item in menu:
                shopping_cart.append(menu[item])
            else:
                continue
            tally_total(shopping_cart)
        except EOFError:
            break

def tally_total(shopping_cart):
    print(f'Total: {sum(shopping_cart):.2f}')

if __name__ == '__main__':
    create_shopping_cart()
