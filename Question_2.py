shopping_list = []

def add_item():
    while True:
        add = input("What items would you like to add to your shopping list?")
        if add == "quit":
            break
        shopping_list.append(add)

def remove_item():
    while True:
        remove = input("What items would you like to remove from your shopping list?")
        if remove == "quit":
            break
        shopping_list.remove(remove)

add_item()
remove_item()
print(f"This is your shopping list: {shopping_list}")