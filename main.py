from apps.auth.views import login, register, logout


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
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
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
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        logout()
        return auth_menu()
    else:
        print("Invalid choice")
    return admin_menu()


if __name__ == "__main__":
    auth_menu()