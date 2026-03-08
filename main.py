from menu import view_menu
from orders import place_order

while True:
    print("\n1 View Menu")
    print("2 Place Order")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        place_order()

    elif choice == "3":
        break