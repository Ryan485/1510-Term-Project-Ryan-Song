import random
import time

monster_list = []


def colours():
    """
    List of colours.

    :postcondition: dictionary containing the color codes for different colors
    :return: list of colours
    # doctest: +SKIP
    """
    return {
        "RED": "\033[91m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "MAGENTA": "\033[95m",
        "RESET": "\033[0m",
        "BOLD": "\033[1m",
    }


def description(color):
    """
    Display available directions to the user and ask them to choose one.

    :precondition: user input has to be a string
    :postcondition: direction is correctly chosen by the user
    :return: direction chosen from the available directions
    # doctest: +SKIP
    """

    description = (f"{color['YELLOW']}Welcome to our Dungeon! Your mission is to kill monsters as many as possible!\n"
                   "Before we continue, you have to choose a character.\n"
                   "Each character has their own unique skills. Choose the character that matches your play style!\n\n")

    for words in description:
        print(words, end="")
        time.sleep(0.01)

    display_character_choices = (f"{color['BLUE']}Please choose your character.\n"
                                 f"{color['MAGENTA']}1. Ranger - Damage: 150 | HP: 100\n"
                                 "2. Wolverine - Damage: 80 | HP: 150\n"
                                 "3. Axeman - Damage: 50 | HP: 200\n\n")
    for texts in display_character_choices:
        print(texts, end="")
        time.sleep(0.01)


def get_user_choice(color):
    while True:
        user_choice = input(f"{color['GREEN']}Please choose your character by number: ")
        if user_choice not in ["1", "2", "3"]:
            print(f"\n{color['RED']}Please choose a valid number from the list!\n")
        else:
            return user_choice


def assign_character(selected_character, color):
    if selected_character == "1":
        print(f"{color['MAGENTA']}Your character is Ranger! Let's go kill monsters!\n")
    elif selected_character == "2":
        print(f"{color['MAGENTA']}Your character is Wolverine! Let's go kill monsters!\n")
    elif selected_character == "3":
        print(f"{color['MAGENTA']}Your character is Axeman! Let's go kill monsters!\n")
    time.sleep(0.5)


def tutorial_description(color):
    instructions = (f"{color['YELLOW']}Now you are in dungeon. '💂' indicates your current location.\n"
                    f"For our next step, we are going to learn how to move.\nPlease move your character TEN times.\n"
                    f"Choose a direction below to move your character.\n\n")
    for words in instructions:
        print(words, end="")
        time.sleep(0.01)


def mock_board(coordinates, rows, columns, color):
    for row in range(rows):
        for column in range(columns):
            coordinates[(0, 0)] = "💂‍♂️"
            current_location = coordinates[(row, column)]
            if current_location == "💂‍♂️":
                print(f"{color['RED']}{current_location}{color['RESET']}", end='  ')
            else:
                print(f"{color['GREEN']}{current_location}{color['RESET']}", end='  ')
        print()


def user_direction(color):
    """
    Display available directions to the user and ask them to choose one.

    :precondition: user input has to be a string
    :postcondition: direction is correctly chosen by the user
    :return: direction chosen from the available directions
    # doctest: +SKIP
    """
    while True:
        directions = input(f"{color['BOLD']}\nChoose the direction "
                           "\n 1. West 2. East 3. North 4. South"
                           "\nEnter a number for directions: ")
        if directions not in ["1", "2", "3", "4"]:
            print("\nPlease choose a valid number between 1 and 4!\n")
        else:
            return directions


def character_attributes(user_choice):
    if user_choice == "1":
        return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 100, "Damage": 150, "Level": 1, "EXP": 0}
    if user_choice == "2":
        return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 150, "Damage": 80, "Level": 1, "EXP": 0}
    if user_choice == "3":
        return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 200, "Damage": 50, "Level": 1, "EXP": 0}


def set_board_coordinates(rows, columns):
    board = {}

    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = '🌲'
    return board


def valid_move(attributes, rows, columns, direction):
    check_x_coordinate = attributes["X-coordinate"]
    check_y_coordinate = attributes["Y-coordinate"]

    if direction == "1":
        check_y_coordinate -= 1
    elif direction == "2":
        check_y_coordinate += 1
    elif direction == "3":
        check_x_coordinate -= 1
    elif direction == "4":
        check_x_coordinate += 1

    if 0 <= check_x_coordinate < rows and 0 <= check_y_coordinate < columns:
        return True
    else:
        print("You can't move in that direction!")
        return False


def user_movement(attributes, coordinates, validation, direction):
    x_coordinate = attributes["X-coordinate"]
    y_coordinate = attributes["Y-coordinate"]

    coordinates[(x_coordinate, y_coordinate)] = "🌲"

    if validation:
        if direction == "1":
            y_coordinate -= 1
        elif direction == "2":
            y_coordinate += 1
        elif direction == "3":
            x_coordinate -= 1
        elif direction == "4":
            x_coordinate += 1

    coordinates[(x_coordinate, y_coordinate)] = "💂‍♂️"
    attributes["X-coordinate"] = x_coordinate
    attributes["Y-coordinate"] = y_coordinate


def tutorial_monster(color):
    words = (f"{color['YELLOW']}\nAs you wander through the dungeon, "
             f"you'll encounter monsters looking like this {color['MAGENTA']}'👹'\n"
             f"{color['YELLOW']}Your mission is to kill them.\n"
             f"When you are low on HP, you can heal yourself at the hospital.\n"
             f"Hospital looks like this: {color['BLUE']}🏥\n"
             f"{color['YELLOW']}Now, let's go and slay some monsters!{color['RESET']}\n\n")

    for word in words:
        print(word, end='')
        time.sleep(0.05)


def display_board(coordinates, rows, columns, color, movement):
    for row in range(rows):
        for column in range(columns):
            new_board = coordinates[(row, column)]
            if new_board == "💂‍♂️":
                print(f"{color['RED']}{new_board}{color['RESET']}", end='  ')
            else:
                print(f"{color['GREEN']}{new_board}{color['RESET']}", end='  ')
        print()


def spawn_monsters(rows, columns):
    coordinates_list = []
    global monster_list

    for row in range(rows):
        for column in range(columns):
            coordinates_list.append((row, column))

    randomly_generated = random.choice(coordinates_list)
    monster_list.append(randomly_generated)

    return randomly_generated


def battle_field(coordinates, rows, columns, color, movement, monsters):
    global monster_list
    for row in range(rows):
        for column in range(columns):
            if (row, column) == monsters:
                coordinates[(row, column)] = "👹"
                coordinates[(3, 5)] = "🏥"
                monster_list.append(monsters)
            new_board = coordinates[(row, column)]
            if new_board == "💂‍♂️":
                print(f"{color['RED']}{new_board}{color['RESET']}", end='  ')
            elif new_board == "👹":
                print(f"{color['MAGENTA']}{new_board}{color['RESET']}", end='  ')
            elif new_board == "🏥":
                print(f"{color['BLUE']}{new_board}{color['RESET']}", end='  ')
            else:
                print(f"{color['GREEN']}{new_board}{color['RESET']}", end='  ')
        print()


def monster_attributes():
    return {"HP": 500, "Damage": 20}


def hospital(attributes, user_choice, color):
    x_coordinate = attributes["X-coordinate"]
    y_coordinate = attributes["Y-coordinate"]
    while (x_coordinate, y_coordinate) == (3, 5):
        user_decision = input(f"{color['BLUE']}Do you want to heal? Y/N: ")
        user_decision.lower()
        if user_decision == "y" or user_decision == "yes":
            if user_choice == "1" and attributes["Level"] == 1:
                attributes["HP"] = 100
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "1" and attributes["Level"] == 2:
                attributes["HP"] = 150
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "1" and attributes["Level"] == 3:
                attributes["HP"] = 200
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "2" and attributes["Level"] == 1:
                attributes["HP"] = 150
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "2" and attributes["Level"] == 2:
                attributes["HP"] = 200
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "2" and attributes["Level"] == 3:
                attributes["HP"] = 400
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "3" and attributes["Level"] == 1:
                attributes["HP"] = 200
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "3" and attributes["Level"] == 2:
                attributes["HP"] = 300
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
            elif user_choice == "3" and attributes["Level"] == 3:
                attributes["HP"] = 500
                print(f"Your HP is fully healed! Your HP is back to {attributes['HP']}!")
                break
        elif user_decision == "n" or user_decision == "no":
            print(f"You are passing the hospital! Come back when you are injured 🙂")
            break
        else:
            print("Invalid entry! Please answer either Y or N!")


def level_2(attributes, user_choice, color):
    if attributes["Level"] == 1 and attributes["EXP"] == 300:
        attributes["Level"] += 1
        print(f"{color['YELLOW']}Congratulations! You are now Level {attributes['Level']}!")
        if user_choice == "1":
            attributes["Damage"] += 50
            attributes["HP"] = 150
            print(f"At Level 2, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}")
        elif user_choice == "2":
            attributes["Damage"] += 20
            attributes["HP"] = 200
            print(f"At Level 2, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}")
        elif user_choice == "3":
            attributes["Damage"] += 20
            attributes["HP"] = 300
            print(f"At Level 2, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}")


def level_3(attributes, user_choice, color):
    if attributes["Level"] == 2 and attributes["EXP"] == 700:
        attributes["Level"] += 1
        print(f"{color['YELLOW']}Congratulations! You are now Level {attributes['Level']}!")
        if user_choice == "1":
            attributes["Damage"] += 100
            attributes["HP"] = 200
            print(f"At Level 3, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}")
        elif user_choice == "2":
            attributes["Damage"] += 40
            attributes["HP"] = 400
            print(f"At Level 3, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}")
        elif user_choice == "3":
            attributes["Damage"] += 40
            attributes["HP"] = 500
            print(f"At Level 3, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}")


def fights(color, attributes, monster_info, user_choice):
    global monster_list
    """
    Check if the player encounters a monster.

    :param monster_container: tuple, the coordinates of the monster
    :param attributes: dictionary, contains the player's current attributes including coordinates
    """
    x_coordinate = attributes["X-coordinate"]
    y_coordinate = attributes["Y-coordinate"]
    monster_hp = monster_info["HP"]
    damage = attributes["Damage"]
    monster_damage = monster_info["Damage"]

    if (x_coordinate, y_coordinate) in monster_list:
        print(f"\n{color['RED']}You encountered a monster! Prepare for battle!\n")
        time.sleep(0.5)

        while monster_hp > 0:
            attack = input(f"{color['RED']}Initiate attack? Y/N?: ")
            lower = attack.lower()

            if lower == "yes" or lower == "y":
                while monster_hp > 0:
                    monster_hp -= damage
                    print(f"{color['MAGENTA']}You've attacked the monster! Their HP is now {monster_hp}.")
                    time.sleep(0.1)
                    if random.random() < 0.25 and monster_hp > 0:
                        attributes["HP"] -= monster_damage
                        print(f"{color['RED']}You've got attacked by the monster! Your HP is now {attributes["HP"]}!")
                        time.sleep(0.1)
                    elif monster_hp <= 0:
                        print(f"\n{color['YELLOW']}You've defeated the monster!\n")
                        attributes["EXP"] += 100
                        print(f"You've earned 100 EXP! Your total EXP is: {attributes["EXP"]}EXP.")

            elif lower == "no" or lower == "n":
                print(f"{color['BLUE']}You've just passed the monster!{color['RESET']}\n")
                time.sleep(1)
                break
            else:
                print("\nPlease enter a valid entry\n")


def boss_attributes():
    return {"Damage": 50, "HP": 1000}


def boss_description(color):
    words = (f"{color['GREEN']}Now that you have reached our MAX Level, "
             f"you need to defeat our final boss to finish this game\n"
             f"The stats for final boss are: Damage: 50 | HP: 1000\n"
             f"The final boss will look like this: 👾\n"
             f"Good luck!\n{color['RESET']}")

    for word in words:
        print(word, end='')
        time.sleep(0.5)


# def boss(attributes, user_choice, color, boss_info):
#     for row in range(rows):
#         for column in range(columns):
#             if (row, column) == monsters:
#                 coordinates[(row, column)] = "👹"
#                 coordinates[(3, 5)] = "🏥"
#                 monster_list.append(monsters)
#             new_board = coordinates[(row, column)]
#             if new_board == "💂‍♂️":
#                 print(f"{color['RED']}{new_board}{color['RESET']}", end='  ')
#             elif new_board == "👹":
#                 print(f"{color['MAGENTA']}{new_board}{color['RESET']}", end='  ')
#             elif new_board == "🏥":
#                 print(f"{color['BLUE']}{new_board}{color['RESET']}", end='  ')
#             else:
#                 print(f"{color['GREEN']}{new_board}{color['RESET']}", end='  ')
#         print()


# def game_over(attributes, user_choice):
#     if attributes["HP"] >= 0:
#         print("Game Over")
#         replay = input("Do you want to play again? Y/N: ")
#         replay.lower()
#         if replay == "yes" or replay == "y":
#             if user_choice == "1":
#                 attributes{"X-coordinate": 0, "Y-coordinate": 0, "HP": 100, "Damage": 150, "Level": 1, "EXP": 0}
#             if user_choice == "2":
#                 return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 150, "Damage": 80, "Level": 1, "EXP": 0}
#             if user_choice == "3":
#                 return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 200, "Damage": 50, "Level": 1, "EXP": 0}


def game():
    rows = 7
    columns = 11
    color = colours()

    coordinates = set_board_coordinates(rows, columns)

    monsters = spawn_monsters(rows, columns)
    # description(color)
    user_choice = get_user_choice(color)
    assign_character(user_choice, color)
    attributes = character_attributes(user_choice)
    monster_info = monster_attributes()
    # tutorial_description(color)

    # mock_board(coordinates, rows, columns, color)
    # time.sleep(0.5)
    # print("\n")
    # count = 0
    # while count < 10:
    #     display_board(coordinates, rows, columns, color, True)
    #     direction = user_direction(color)
    #
    #     if valid_move(attributes, rows, columns, direction):
    #         user_movement(attributes, coordinates, True, direction)
    #
    #     count += 1
    #
    # print(f"{color['YELLOW']}\nCongratulations! You've mastered how to move!{color['RESET']}")
    # tutorial_monster(color)

    while attributes["HP"] >= 0 or attributes["Level"] < 3:
        monsters = spawn_monsters(rows, columns)
        battle_field(coordinates, rows, columns, color, True, monsters)

        direction = user_direction(color)
        if attributes["Level"] == 3:
            break
        if valid_move(attributes, rows, columns, direction):
            user_movement(attributes, coordinates, True, direction)
            if level_2(attributes, user_choice, color):
                level_2(attributes, user_choice, color)
            elif hospital(attributes, user_choice, color):
                hospital(attributes, user_choice, color)
            elif level_3(attributes, user_choice, color):
                level_3(attributes, user_choice, color)
            else:
                fights(color, attributes, monster_info, user_choice)

    boss_description(color)


def main():
    """
    Drive the game
    """
    game()


if __name__ == "__main__":
    main()
