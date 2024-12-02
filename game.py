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

    # doctest: +SKIP
    """

    description = (f"{color['YELLOW']}Welcome to our Dungeon! Your mission is to kill monsters as many as possible!\n"
                   "Before we continue, you have to choose a character.\n"
                   "Each character has their own unique skills. Choose the character that matches your play style!\n\n")

    for words in description:
        print(words, end="")
        time.sleep(0.05)

    display_character_choices = (f"{color['BLUE']}Please choose your character.\n"
                                 f"{color['MAGENTA']}1. Ranger - Damage: 150 | HP: 100\n"
                                 "2. Wolverine - Damage: 80 | HP: 150\n"
                                 "3. Axeman - Damage: 50 | HP: 200\n\n")
    for texts in display_character_choices:
        print(texts, end="")
        time.sleep(0.05)


def get_user_choice(color):
    """
    Let user choose their character.

    :param color: color attributes for texts
    :precondition: user input has to be a string
    :postcondition: store user choice
    :return: user character choice

    # doctest: +SKIP
    """
    while True:
        user_choice = input(f"{color['GREEN']}Please choose your character by number: ")
        if user_choice not in ["1", "2", "3"]:
            print(f"\n{color['RED']}Please choose a valid number from the list!\n")
        else:
            return user_choice


def assign_character(selected_character, color):
    """
    Show user their selected character.

    :param selected_character: selected character from the user
    :param color: color attributes for texts
    :precondition: character is successfully chosen by the user
    :postcondition: successfully display the prompt based on the user choice

    # doctest: +SKIP
    """
    if selected_character == "1":
        print(f"{color['MAGENTA']}Your character is Ranger! Let's go kill monsters!\n")
    elif selected_character == "2":
        print(f"{color['MAGENTA']}Your character is Wolverine! Let's go kill monsters!\n")
    elif selected_character == "3":
        print(f"{color['MAGENTA']}Your character is Axeman! Let's go kill monsters!\n")
    time.sleep(0.5)


def tutorial_description(color):
    """
    A brief description of the tutorial.

    :param color: color attributes for texts
    :precondition: color is successfully called from colours()
    :postcondition: tutorial description is successfully displayed

    # doctest: +SKIP
    """
    instructions = (f"{color['YELLOW']}Now you are in dungeon. '💂' indicates your current location.\n"
                    f"For our next step, we are going to learn how to move.\nPlease move your character TEN times.\n"
                    f"Choose a direction below to move your character.\n\n")
    for words in instructions:
        print(words, end="")
        time.sleep(0.05)


def set_board_coordinates(rows, columns):
    """
    Assign coordinates to a board using a dictionary.

    :param rows: rows of board
    :param columns: columns of board
    :precondition: rows and columns are integers
    :postcondition: the board coordinates are successfully assigned
    :return: a dictionary that contains coordinate as a key and a tree emoji as a value

    >>> set_board_coordinates(1, 1)
    {(0, 0): '🌲'}
    >>> set_board_coordinates(2, 2)
    {(0, 0): '🌲', (0, 1): '🌲', (1, 0): '🌲', (1, 1): '🌲'}
    """
    board = {}

    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = '🌲'
    return board


def mock_board(coordinates, rows, columns):
    """
    Display the board and the character's location to the user.

    Provides a visual representation of the board to help users understand its dynamics.

    :param coordinates: assigned coordinates for the board
    :param rows: rows of board
    :param columns: columns of board
    :precondition coordinates: coordinates are successfully assigned
    :precondition rows: rows are integers
    :precondition columns: columns are integers
    :postcondition: board and the user character are successfully displayed

    # doctest: +SKIP
    """
    for row in range(rows):
        for column in range(columns):
            coordinates[(0, 0)] = "💂‍♂️"
            current_location = coordinates[(row, column)]
            if current_location == "💂‍♂️":
                print(f"{current_location}", end='  ')
            else:
                print(f"{current_location}", end='  ')
        print()


def user_direction(color):
    """
    Display available directions to the user and ask them to choose one.

    :param color: color attributes for texts
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
    """
    Set character's attributes.

    :param user_choice: selected character from the user
    :precondtion: character is selected from the user
    :postcondition: character's attributes are successfully assigned'
    :return: a dictionary containing the character's attributes based on the user choice

    # doctest: +SKIP
    """
    if user_choice == "1":
        return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 100, "Damage": 150, "Level": 1, "EXP": 0}
    if user_choice == "2":
        return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 150, "Damage": 80, "Level": 1, "EXP": 0}
    if user_choice == "3":
        return {"X-coordinate": 0, "Y-coordinate": 0, "HP": 200, "Damage": 50, "Level": 1, "EXP": 0}


def valid_move(attributes, rows, columns, direction):
    """
    Check if the character moves to the right direction.

    :param attributes: character attributes
    :param rows: rows of board
    :param columns: columns of board
    :param direction: direction chosen by the user
    :precondition attributes: character's attributes are successfully assigned
    :precondition rows: rows are integers
    :precondition columns: columns are integers
    :postcondition direction: direction is correctly chosen by the user
    :return: boolean value based on the user direction

    >>> attributes = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 100, "Damage": 150, "Level": 1, "EXP": 0}
    >>> valid_move(attributes, 3, 3, "2")
    True
    >>> attributes = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 100, "Damage": 150, "Level": 1, "EXP": 0}
    >>> valid_move(attributes, 3, 3, "1")
    You can't move in that direction!
    False
    """
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
    """
    Update the user's coordinates based on their direction choice.

    :param attributes: character attributes
    :param coordinates: assigned coordinates for the board
    :param validation: boolean value determining whether the user moves
    :param direction: direction chosen by the user
    :precondition attributes: character's attributes are successfully assigned
    :precondition coordinates: coordinates are correctly assigned
    :precondition validation: boolean value is properly set
    :precondition direction: direction is correctly chosen by the user
    :postcondition attributes: character's attributes are correctly updated
    :postcondition coordinates: coordinates are correctly updated

    #doctest: +SKIP
    """
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
    """
    A brief explanation about monsters and the hospital.

    :param color: color attributes for texts
    :precondition color: color attributes are called successfully
    :postcondition: description is successfully displayed

    #doctest: +SKIP
    """
    words = (f"{color['YELLOW']}\nAs you wander through the dungeon, "
             f"you'll encounter monsters looking like this '👹'\n"
             f"{color['YELLOW']}Your mission is to kill them.\n"
             f"When you are low on HP, you can heal yourself at the hospital.\n"
             f"Hospital looks like this: 🏥\n"
             f"{color['YELLOW']}Now, let's go and slay some monsters!{color['RESET']}\n\n")

    for word in words:
        print(word, end='')
        time.sleep(0.05)


def display_board(coordinates, rows, columns):
    """
    Display the game board to the user.

    :param coordinates: assigned coordinates for the board
    :param rows: rows of the board
    :param columns: columns of the board
    :precondition coordinates: coordinates are correctly assigned
    :precondition rows: rows are integers
    :precondition columns: columns are integers
    :postcondition: the board is displayed correctly based on the coordinates.

    #doctest: +SKIP
    """
    for row in range(rows):
        for column in range(columns):
            new_board = coordinates[(row, column)]
            if new_board == "💂‍♂️":
                print(f"{new_board}", end='  ')
            else:
                print(f"{new_board}", end='  ')
        print()


def spawn_monsters(rows, columns):
    """
    Randomly choose coordinates generated from the for loop and store it in the monster_list dictionary.

    :param rows: rows of the board
    :param columns: rows of the board
    :precondition rows: rows are integers
    :precondition columns: columns are integers
    :postcondition: a coordinate is randomly selected and is stored in the monster_list
    :return: a randomly selected coordinate

    #doctest: +SKIP
    """
    coordinates_list = []
    global monster_list

    for row in range(rows):
        for column in range(columns):
            coordinates_list.append((row, column))

    randomly_generated = random.choice(coordinates_list)
    monster_list.append(randomly_generated)

    return randomly_generated


def battle_field(coordinates, rows, columns, color, monsters):
    """
    Visualize monsters and the hospital based on their coordinates.

    :param coordinates: assigned coordinates for the board
    :param rows: rows of the board
    :param columns: columns of the board
    :param color: color attributes to reset colours
    :param monsters: a randomly selected coordinate
    :precondition coordinates: coordinates are correctly assigned
    :precondition rows: rows are integers
    :precondition columns: columns are integers
    :precondition monsters: coordinate is within the range of rows and columns
    :postcondition: monsters and the hospital are displayed correctly based on the coordinates.

    #doctest: +SKIP
    """
    global monster_list
    for row in range(rows):
        for column in range(columns):
            if (row, column) == monsters:
                coordinates[(row, column)] = "👹"
                coordinates[(3, 5)] = "🏥"
                monster_list.append(monsters)
            new_board = coordinates[(row, column)]
            if new_board == "💂‍♂️":
                print(f"{new_board}{color['RESET']}", end='  ')
            elif new_board == "👹":
                print(f"{new_board}{color['RESET']}", end='  ')
            elif new_board == "🏥":
                print(f"{new_board}{color['RESET']}", end='  ')
            else:
                print(f"{new_board}{color['RESET']}", end='  ')
        print()


def monster_attributes():
    """
    Set monster attributes

    :return: monster attributes

    #doctest: +SKIP
    """
    return {"HP": 500, "Damage": 20}


def hospital(attributes, user_choice, color):
    """
    Heal the player's character based on their level, and character choice.

    :param attributes: character's attributes
    :param user_choice: character chosen by the user
    :param color: color attributes
    :precondition attributes: attributes are properly set
    :precondtion user_choice: character is correctly chosen by the user
    :precondition color: color attributes are properly set
    :postcondition: character is healed according their attributes

    #doctest: +SKIP
    """
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
    """
    Tell the user that they have leveled up and show their new attributes.

    :param attributes: character's attributes
    :param user_choice: character chosen by the user
    :param color: color attributes
    :precondition attributes: attributes satisfy requirements to level up
    :precondition user_choice: character is correctly chosen by the user
    :precondition color: color attributes are properly set
    :postcondition: character is leveled up and their attributes are updated according to their character choice

    #doctest: +SKIP
    """
    if attributes["Level"] == 1 and attributes["EXP"] == 300:
        attributes["Level"] += 1
        print(f"{color['YELLOW']}Congratulations! You are now Level {attributes['Level']}!")
        if user_choice == "1":
            attributes["Damage"] += 50
            attributes["HP"] = 150
            print(f"At Level 2, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}\n")
        elif user_choice == "2":
            attributes["Damage"] += 20
            attributes["HP"] = 200
            print(f"At Level 2, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}\n")
        elif user_choice == "3":
            attributes["Damage"] += 20
            attributes["HP"] = 300
            print(f"At Level 2, Your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}\n")


def level_3(attributes, user_choice, color):
    """
    Tell the user that they have leveled up and show their new attributes.

    :param attributes: character's attributes
    :param user_choice: character chosen by the user
    :param color: color attributes
    :precondition attributes: attributes satisfy requirements to level up
    :precondition user_choice: character is correctly chosen by the user
    :precondition color: color attributes are properly set
    :postcondition: character is leveled up and their attributes are updated according to their character choice

    #doctest: +SKIP
    """
    if attributes["Level"] == 2 and attributes["EXP"] == 700:
        attributes["Level"] += 1
        print(f"\n{color['YELLOW']}Congratulations! You are now Level {attributes['Level']}!")
        if user_choice == "1":
            attributes["Damage"] += 100
            attributes["HP"] = 200
            print(f"At Level 3, your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}\n")
        elif user_choice == "2":
            attributes["Damage"] += 40
            attributes["HP"] = 400
            print(f"At Level 3, your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}\n")
        elif user_choice == "3":
            attributes["Damage"] += 40
            attributes["HP"] = 500
            print(f"At Level 3, your character's stat is: "
                  f"Damage | {attributes['Damage']} | HP | {attributes['HP']}{color['RESET']}\n")


def fights(color, attributes, monster_info, user_choice):
    """

    :param color:
    :param attributes:
    :param monster_info:
    :param user_choice:
    """
    global monster_list
    x_coordinate = attributes["X-coordinate"]
    y_coordinate = attributes["Y-coordinate"]
    monster_hp = monster_info["HP"]
    damage = attributes["Damage"]
    monster_damage = monster_info["Damage"]

    if (x_coordinate, y_coordinate) in monster_list:
        print(f"\n{color['RED']}You encountered a monster! Prepare for battle!\n")
        time.sleep(0.5)

        while monster_hp > 0:
            if attributes["HP"] <= 0:
                break
            attack = input(f"{color['RED']}Initiate attack? Y/N?: ")
            lower = attack.lower()

            if lower == "yes" or lower == "y":
                while monster_hp > 0:
                    if attributes["HP"] <= 0:
                        break
                    monster_hp -= damage
                    print(f"{color['MAGENTA']}You've attacked the monster! Their HP is now {monster_hp}.")
                    time.sleep(0.5)
                    if random.random() < 0.25 and monster_hp > 0:
                        attributes["HP"] -= monster_damage
                        print(f"{color['RED']}You've got attacked by the monster! Your HP is now {attributes["HP"]}!")
                        time.sleep(0.5)
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
    """
    Set boss attributes.

    :return: boss attributes

    #doctest: +SKIP
    """
    return {"Damage": 200, "HP": 2000}


def boss_description(color):
    """
    An explanation of boss appearance and how the user can take advantage of the new healing system.

    :param color: color attributes
    :precondition color: color attributes are properly set
    :postcondition: the description is successfully displayed

    #doctest: +SKIP
    """
    words = (f"{color['GREEN']}Now that you have reached our MAX Level, "
             f"you need to defeat our final boss to finish this game.\n\n"
             f"{color['MAGENTA']}The stats for final boss are: Damage: 200 | HP: 2000\n\n"
             f"{color['YELLOW']}The final boss will look like this: 👾\n\n"
             f"{color['GREEN']}Since you are fighting the boss, extra HP will be given when you visit the hospital.\n"
             f"Make sure you take advantage of this before fighting the boss!\n\n"
             f"{color['BLUE']}The final boss has absorbed all the monsters' energy, leaving them static.\n"
             f"You can pass through monsters without fighting.\n\n"
             f"Good luck!\n{color['RESET']}\n")

    for word in words:
        print(word, end='')
        time.sleep(0.05)


def boss(coordinates, rows, columns, movement, attributes, final_boss, color):
    x_coordinate = attributes["X-coordinate"]
    y_coordinate = attributes["Y-coordinate"]
    boss_hp = final_boss["HP"]
    boss_damage = final_boss["Damage"]
    damage = attributes["Damage"]

    board = {}

    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = '🌲'

    for row in range(rows):
        for column in range(columns):
            coordinates[(3, 3)] = "👾"
            coordinates[(3, 5)] = "🏥"
            board = coordinates[(row, column)]
            print(f"{board}", end='  ')
        print()

    while (x_coordinate, y_coordinate) == (3, 5):
        user_decision = input(f"{color['BLUE']}Do you want to heal? Y/N: ").lower()
        if user_decision in ("y", "yes"):
            attributes["HP"] += 500
            print(
                f"We gave you extra HP to prepare you for the boss! Your HP is now {attributes['HP']}{color['RESET']}\n")
            break
        elif user_decision in ("n", "no"):
            print(f"You have passed the hospital!{color['RESET']}\n")
            break

    while (x_coordinate, y_coordinate) == (3, 3):
        if attributes["HP"] <= 0:
            print("You died fighting the boss!")
            return False
        elif boss_hp <= 0:
            print("You finished the game!")
            final_boss["HP"] = 0
            return False

        decision = input(f"\n{color['RED']}Ready to fight the boss? Y/N: ").lower()
        if decision in ("yes", "y"):
            while boss_hp > 0:
                boss_hp -= damage
                print(f"{color['MAGENTA']}You've attacked the boss! Their HP is now {boss_hp}.")
                time.sleep(1)

                if boss_hp <= 0:
                    print(f"\n{color['BLUE']}Congratulations! You have defeated the final boss!{color['RESET']}\n")
                    final_boss["HP"] = 0
                    last_message(color)
                    return False

                if random.random() < 0.25:
                    attributes["HP"] -= boss_damage
                    print(f"{color['RED']}You've been attacked by the monster! Your HP is now {attributes['HP']}.")
                    time.sleep(1)

                if attributes["HP"] <= 0:
                    print("\nYou died fighting the boss!\n\n"
                          "Game Over. See you next time!")
                    return False

        elif decision in ("no", "n"):
            print(f"You've passed the monster!{color['RESET']}")
            return True

    return True


def last_message(color):
    """
    Tell the user that they have successfully completed the game.

    :param color: color attributes
    :precondition: color attributes are properly set
    :postcondition: the description is correctly displayed

    #doctest: +SKIP
    """
    message = (f"\n{color['YELLOW']}You have successfully completed this game!\n"
               f"You will be remembered as a legend in this dungeon....")
    for word in message:
        print(word, end='')
        time.sleep(0.07)


def game():
    rows = 7
    columns = 11
    color = colours()

    coordinates = set_board_coordinates(rows, columns)

    monsters = spawn_monsters(rows, columns)
    description(color)
    user_choice = get_user_choice(color)
    assign_character(user_choice, color)
    attributes = character_attributes(user_choice)
    monster_info = monster_attributes()
    final_boss = boss_attributes()
    tutorial_description(color)

    mock_board(coordinates, rows, columns)
    time.sleep(0.5)
    print("\n")
    count = 0
    while count < 10:
        display_board(coordinates, rows, columns)
        direction = user_direction(color)

        if valid_move(attributes, rows, columns, direction):
            user_movement(attributes, coordinates, True, direction)

        count += 1

    print(f"{color['YELLOW']}\nCongratulations! You've mastered how to move!{color['RESET']}")
    tutorial_monster(color)

    while attributes["HP"] >= 0 and attributes["Level"] < 3:

        monsters = spawn_monsters(rows, columns)
        battle_field(coordinates, rows, columns, color, monsters)

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

        if attributes["HP"] <= 0:
            print("\nYOU DIED!!\n")

        while attributes["HP"] <= 0:
            replay = input("Do you want to respawn? Y/N: ")
            replay.lower()
            if replay == "yes" or replay == "y":
                attributes["HP"] += 200
                print(f"You have been revived! Your HP is now {attributes['HP']}")
                continue
            elif replay == "no" or replay == "n":
                print("\nGame Over. See you next time!")
                break
            else:
                print("Please enter a valid entry\n")

    boss_description(color)

    while attributes["HP"] > 0 and final_boss["HP"] > 0:
        if not boss(coordinates, rows, columns, True, attributes, final_boss, color):
            break

        direction = user_direction(color)

        if valid_move(attributes, rows, columns, direction):
            user_movement(attributes, coordinates, True, direction)


def main():
    """
    Drive the game
    """
    game()


if __name__ == "__main__":
    main()
