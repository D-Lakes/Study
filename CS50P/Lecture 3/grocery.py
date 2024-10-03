def grocery_list():
    grocery_list = get_grocery_list()
    analyze_grocery_list(grocery_list)

def get_grocery_list():
    grocery_list = []
    while True:
        try:
            grocery_list.append(input().upper())
        except EOFError:
            return grocery_list

def analyze_grocery_list(grocery_list: list):
    unique_items = list(set(grocery_list))

    for item in unique_items:
        print(grocery_list.count(item), item)


if __name__ == '__main__':
    grocery_list()
