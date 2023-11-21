import os

admin_user = "Bob"

if os.path.exists("admin.dat"):

    # The file exists, so open the file for reading (`"r"`), and read
    # the string data, storing it in our variable `admin_user`
    file = open("admin.dat", "r")
    admin_user = file.read()
    file.close()

    # Strip off any whitespace like spaces, tabs, or newlines from the
    # beginning and end of the string
    admin_user = admin_user.strip()

    # Split the string up by newlines (creating a list), in case the
    # file was manually edited and contains more than one line of data.
    # Then select the first item in the list, using index 0 (`[0]`).
    admin_user = admin_user.split("\n")[0]

else:

    # The file does not exist, so create the file by opening it for
    # writing (`"w"`), and then write the data stored in our variable
    # `admin_user` to the file.
    file = open("admin.dat", "w")
    file.write(admin_user)
    file.close()


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
        file = open("admin.dat", "w")
        file.write(admin_user)
        file.close()


    else:
        print(f'Error: Selected option "{selected_option}" is invalid!')
