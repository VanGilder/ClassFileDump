admin_user = "Bob"

while True:
    print("=====================================================")
    print(f"Hello {admin_user}, what would you like to do today?")
    print()
    print('  1) Say "Hello" and continue with program.')
    print('  2) Say "Goodbye" and exit program.')
    print('  3) Change user name.')
    print()
    selected_option = input("Select an option (by option number): ")
    print("-----------------------------------------------------")

    if selected_option == "1":
        print(f"Hello {admin_user}.")
        # The `continue` keyword stops this current iteration of the loop's execution,
        # and begins code execution from the top of the loop (checking the condition).
        continue

    elif selected_option == "2":
        print(f"Goodbye {admin_user}.")
        # The `break` keyword stops this current iteration of the loop's execution,
        # and ends the loop entirely.
        break

    elif selected_option == "3":
        admin_user = input("What would you like to change the username to? ")

    else:
        print(f'Error: Selected option "{selected_option}" is invalid!')
