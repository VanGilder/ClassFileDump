def main_game_loop():
    print("Welcome to the Adventure!")
    print("Would you like to:")
    print("1. Create a new character")
    print("2. Use a pre-defined character")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        player_character = create_custom_character()
    elif choice == '2':
        print("Select a pre-defined character:")
        print("1. Nameora - Half-elven messenger")
        print("2. Saad Amina - Work-for-hire herbalist")

        predef_choice = input("Enter your choice (1/2): ")

        if predef_choice == '1':
            player_character = nameora
        elif predef_choice == '2':
            player_character = saad
        else:
            print("Invalid choice. Exiting.")
            return
    else:
        print("Invalid choice. Exiting.")
        return

    # The rest of your game loop here, using player_character as the main character.




# Define skill points and choices for Classes and Races
initial_skill_points = 10

# 8 general D&D classes
classes_choices = [
    "Wizard",
    "Warrior",
    "Rogue",
    "Cleric",
    "Paladin",
    "Ranger",
    "Sorcerer",
    "Druid"
]

# 8 general D&D races
races_choices = [
    "Human",
    "Elf",
    "Dwarf",
    "Halfling",
    "Orc",
    "Gnome",
    "Dragonborn",
    "Tiefling"
]

# Function to handle character creation for a custom character
def create_custom_character():
    print("\n--- Custom Character Creation ---")

    # Skill point allocation
    skill_points = initial_skill_points
    skills = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }

    print(f"You have {skill_points} skill points to allocate.")
    for skill in skills.keys():
        while True:
            try:
                points = int(input(f"Allocate points for {skill}: "))
                if points <= skill_points and points >= 0:
                    skills[skill] = points
                    skill_points -= points
                    print(f"{skill_points} skill points remaining.")
                    break
                else:
                    print("Invalid input. Please allocate within your remaining skill points.")
            except ValueError:
                print("Please enter a number.")

    # Class selection
    print("\nChoose a Class:")
    for i, class_choice in enumerate(classes_choices):
        print(f"{i+1}. {class_choice}")

    while True:
        try:
            class_selection = int(input("Your choice: "))
            if 1 <= class_selection <= len(classes_choices):
                chosen_class = classes_choices[class_selection - 1]
                break
            else:
                print("Invalid choice. Select a number corresponding to the classes.")
        except ValueError:
            print("Please enter a number.")

    # Race selection
    print("\nChoose a Race:")
    for i, race_choice in enumerate(races_choices):
        print(f"{i+1}. {race_choice}")

    while True:
        try:
            race_selection = int(input("Your choice: "))
            if 1 <= race_selection <= len(races_choices):
                chosen_race = races_choices[race_selection - 1]
                break
            else:
                print("Invalid choice. Select a number corresponding to the races.")
        except ValueError:
            print("Please enter a number.")

    custom_character = {
        'Name': 'Custom',
        'Class': chosen_class,
        'Race': chosen_race,
        'Skills': skills
    }

    print("\nYour custom character has been created!")
    print(custom_character)
    return custom_character

# Uncomment the following line to test the function
create_custom_character()
