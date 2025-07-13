from apps.auth.views import login, register, logout
from apps.views.admin_views import add_products, delete_products, show_orders
from apps.views.user_views import add_orders, show_my_orders
from apps.views.views import show_products


def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        if register():
            print("Successfully registered")
        else:
            print("Something went wrong")
    elif choice == "2":
        result = login()
        if result == "admin":
            print("Welcome admin")
            return admin_menu()
        elif result == "user":
            print("Welcome user")
            return user_menu()
        else:
            return login()
    elif choice == "3":
        print("Good bye")
        return
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
    1. Add products
    2. Delete products
    3. Show products
    4. Show orders
    5. Logout
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        add_products()
    elif choice == "2":
        delete_products()
    elif choice == "3":
        show_products()
    elif choice == "4":
        show_orders()
    elif choice == "5":
        logout()
        return auth_menu()
    else:
        print("Invalid choice")
    return admin_menu()


def user_menu():
    print("""
    1. Show products
    2. Add orders
    3. Show my orders
    4. Logout
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        show_products()
    elif choice == "2":
        add_orders()
    elif choice == "3":
        show_my_orders()
    elif choice == "4":
        logout()
        return auth_menu()
    else:
        print("Invalid choice")
    return user_menu()


if __name__ == "__main__":
    auth_menu()