# The initial program to introduce the player to the world and ask for character choice

def intro_and_character_choice():
    print("Welcome, adventurer, to a world of mystery, danger, and untold riches.")
    print("You are about to embark on a journey through treacherous swamps, haunted ruins, and mystical lands.")
    print("Your choices will determine your fate, and perhaps the fate of the world.")
    print("")
    print("Who will you be in this epic tale?")
    print("1. Nameora Littleton - A half-elven messenger with a mysterious past.")
    print("2. Saad Amina - A work-for-hire herbalist with a knack for natural remedies.")
    print("3. Create your own character.")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        return 'Nameora'
    elif choice == '2':
        return 'Saad'
    elif choice == '3':
        return 'Custom'
    else:
        print("Invalid choice. The adventure ends before it began.")
        return None

#Testing the function
choice = intro_and_character_choice()
print(f"You chose: {choice}")
