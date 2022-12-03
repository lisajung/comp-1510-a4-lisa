"""
Lisa Jung
A01332998
"""
import random


NAME_KEY = "Name"
X_COORD_KEY = "X-coordinate"
Y_COORD_KEY = "Y-coordinate"
CURRENT_EGO_KEY = "Current Ego"
MAX_EGO_KEY = "Max Ego"
LEVEL_KEY = "Character Level"
EXP_KEY = "Experience"


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    challenge_addition(character)
    while not achieved_goal and character[CURRENT_EGO_KEY] > 0:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            #describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(character, board)
            if there_is_a_challenge:
                print("Found a challenge")
                execute_challenge_protocol(character, board)
                # if character_has_leveled():
                #     execute_glow_up_protocol()
            else:
                print("No challenge here")
    #             if character_has_leveled():
    #                 execute_glow_up_protocol()
    #         achieved_goal = check_if_goal_attained(board, character)
        else:
            print("That's a wall smarty pants. Choose another direction.")
    #         // Tell the user they can’t go in that direction
    #         // Print end of game stuff like congratulations or sorry you died


def make_character():
    character_name = input("Oh hey....buddy...welcome to finals season! "
                           "We've placed study sessions in classrooms \nthroughout the school for you to "
                           "prepare for finals! \n\nPlease write your name on this nametag *give you nametag* : ")
    return {NAME_KEY: character_name, X_COORD_KEY: 0, Y_COORD_KEY: 0, CURRENT_EGO_KEY: 100, MAX_EGO_KEY: 100, LEVEL_KEY: 1, EXP_KEY: 0}


def check_for_level_up_two(character):
    if character[EXP_KEY] == 100:
        print(r"""
                    ╭╮╱╱╱╱╱╱╱╱╱╭╮
                    ┃┃╱╱╱╱╱╱╱╱╱┃┃
                    ┃┃╭━━┳╮╭┳━━┫┃╱╭╮╭┳━━╮
                    ┃┃┃┃━┫╰╯┃┃━┫┃╱┃┃┃┃╭╮┃
                    ┃╰┫┃━╋╮╭┫┃━┫╰╮┃╰╯┃╰╯┃
                    ╰━┻━━╯╰╯╰━━┻━╯╰━━┫╭━╯
                    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
                    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
        """)
        print("Congrats! You are now level 2!")
        character[LEVEL_KEY] += 1
        character[CURRENT_EGO_KEY] = 100
    else:
        return


def check_for_level_up_three(character):
    if character[EXP_KEY] == 250:
        print(r"""\
                    ╭╮╱╱╱╱╱╱╱╱╱╭╮
                    ┃┃╱╱╱╱╱╱╱╱╱┃┃
                    ┃┃╭━━┳╮╭┳━━┫┃╱╭╮╭┳━━╮
                    ┃┃┃┃━┫╰╯┃┃━┫┃╱┃┃┃┃╭╮┃
                    ┃╰┫┃━╋╮╭┫┃━┫╰╮┃╰╯┃╰╯┃
                    ╰━┻━━╯╰╯╰━━┻━╯╰━━┫╭━╯
                    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
                    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
        """)
        print("Congrats! You are now level 3!")
        character[LEVEL_KEY] += 3
    else:
        return


def challenge_addition(character):
    print("Time for addition!")
    if character[LEVEL_KEY] == 1:
        print("What is 5 + 5?")
        print("a: 30")
        print("b: 16")
        print("c: 5")
        print("d: 10")
        answer = input("Choose one of a, b, c, or d. Type your answer here:")
        if answer.lower() == "d":
            character[EXP_KEY] = character[EXP_KEY] + 50
            print(character)
            check_for_level_up_two(character)
        else:
            character[CURRENT_EGO_KEY] = character[CURRENT_EGO_KEY] - 100
            if character[CURRENT_EGO_KEY] == 0:
                print("game over")
    # elif character[LEVEL_KEY] == 2:
    #     print("What is 36 + 17?")
    #     print("a: 54")
    #     print("b: 53")
    #     print("c: 52")
    #     print("d: 56")
    #     character_answer = input("Choose one of a, b, c, or d. Type your answer here:")
    #     if character_answer.lower == "b":
    #         character[EXP_KEY] = character[EXP_KEY] + 50
    #         check_for_level_up_three(character)
    #     else:
    #         character[CURRENT_EGO_KEY] = character[CURRENT_EGO_KEY] - 50
    #         if character[CURRENT_EGO_KEY] == 0:
    #             print("game over")


def challenge_subtraction():
    print("Time for subtraction!")


def challenge_multiplication():
    print("Time for multiplication!")


def challenge_division():
    print("Time for division!")


def challenge_derivatives():
    print("Time for derivatives!")


def challenge_integrals():
    print("Time for integrals!")



"""This dictionary represents the classroom description as the key and the challenge function that corresponds with 
the class. """
CLASSES = {"Addition": challenge_addition, "Subtraction": challenge_subtraction,
           "Multiplication": challenge_multiplication, "Division": challenge_division,
           "Derivatives": challenge_derivatives, "Integrals": challenge_integrals}


def make_board(rows, columns):
    """
    This function creates the board the player can traverse.
    :param rows: number of rows
    :param columns: number of columns
    :return: a map of the board as a dictionary where the key is the location and the value is the class description.
    """
    possible_locations = []
    # Generate all the possible location tuples
    for row in range(rows):
        for column in range(columns):
            possible_locations.append((row, column))
    # Generate a random selection of class locations for our classes
    possible_classroom_locations = possible_locations
    possible_classroom_locations.remove((0, 0))
    classroom_locations = random.sample(possible_classroom_locations, len(CLASSES))
    print(classroom_locations)
    board = {}
    # Populate an "empty room" board with the keys being the location and the value being the description.
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = "empty room"
    # Replace all locations that have a class with the given class's description
    class_descriptions = list(CLASSES.keys())
    for index in range(len(classroom_locations)):
        board[classroom_locations[index]] = class_descriptions[index]
    return board


def get_character_location(character):
    """
    Retreive the character's location on the board.
    :param character: a dictionary representing the character
    :return: a tuple representing the character's location
    """
    character_location = (character[X_COORD_KEY], character[Y_COORD_KEY])
    return character_location


def describe_current_location(board, character):
    """
    This function describes where the character is on the board.
    :param board: a dictionary representing the game board
    :param character: a dictionary representing the character
    """
    location = board[get_character_location(character)]
    print("You are currently at " + location + ".")
    print("The coordinates of the room you are in are (" + str(get_character_location(character)[0])
          + ", " + str(get_character_location(character)[1]) + ")")


def which_direction():
    """
    Generates an enumerated list representing the direction a user can move
    :return: an enumerated list of all possible directions a user can travel
    """
    possible_directions = ["North", "East", "South", "West"]
    for i, direction in enumerate(possible_directions, 1):
        print(i, ":", direction)


def get_user_choice():
    """
    Ask user which direction they want to move on the board.
    :param character_location: a tuple representing the character's location
    :return: a tuple representing the coordinates the user wishes to travel to
    """
    print("Lets go to a different room. Which direction should we go?")
    which_direction()
    ask_which_direction = input("\nChoose a direction by typing one of the following (1, 2, 3, or 4):")
    if ask_which_direction == "1" or ask_which_direction == "2" or ask_which_direction == "3" or ask_which_direction == "4":
        return int(ask_which_direction)
    else:
        print("There's no room in that direction. Let's choose another direction!")
        return get_user_choice()


def validate_move(character, direction_chosen):
    location = get_character_location(character)
    if direction_chosen == 1:
        return location[1] != 0
    if direction_chosen == 2:
        return location[0] != 4
    if direction_chosen == 3:
        return location[1] != 4
    if direction_chosen == 4:
        return location[0] != 0
    return False


def move_character(character, direction):
    if direction == 1:
        character[Y_COORD_KEY] = character[Y_COORD_KEY] - 1
    elif direction == 2:
        character[X_COORD_KEY] = character[X_COORD_KEY] + 1
    elif direction == 3:
        character[Y_COORD_KEY] = character[Y_COORD_KEY] + 1
    elif direction == 4:
        character[X_COORD_KEY] = character[X_COORD_KEY] - 1


def check_for_challenges(character, board):
    location = board[get_character_location(character)]
    return location in CLASSES.keys()


def execute_challenge_protocol(character, board):
    print(character)
    location = board[get_character_location(character)]
    CLASSES[location](character)


def main():
    game()


if __name__ == "__main__":
    main()
