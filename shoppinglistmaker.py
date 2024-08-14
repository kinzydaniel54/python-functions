def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"Added {item} to the shopping list.")

def remove_item(shopping_list, item):
    try:
        shopping_list.remove(item)
        print(f"Removed {item} from the shopping list.")
    except ValueError:
        print(f"{item} was not found in the shopping list.")

def print_list(shopping_list):
    print("\nShopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print()
#Typing just print will print out the enire list
def main():
    shopping_list = []
    while True:
        action = input("Would you like to add, remove, print the list, or quit? ").lower()
        if action == 'add':
            item_to_add = input("Enter the item to add: ")
            add_item(shopping_list, item_to_add)
        elif action == 'remove':
            item_to_remove = input("Enter the item to remove: ")
            remove_item(shopping_list, item_to_remove)
        elif action == 'print':
            print_list(shopping_list)
        elif action == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose add, remove, print, or quit.")

if __name__ == "__main__":
    main()