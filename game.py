"""
Lisa Jung
A01332998
"""
import random
import sys

NAME_KEY = "Name"
X_COORD_KEY = "X-coordinate"
Y_COORD_KEY = "Y-coordinate"
CURRENT_EGO_KEY = "Current Ego"
MAX_EGO_KEY = "Max Ego"
LEVEL_KEY = "Character Level"
EXP_KEY = "Experience"
POSSIBLE_MULTIPLE_CHOICE_ANSWERS = ["a", "b", "c", "d"]


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    execute_challenge_protocol(character, board)
    check_game_over(character)
    while not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            # describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges(character, board)
            if there_is_a_challenge:
                print("Found a challenge")
                execute_challenge_protocol(character, board)
                check_game_over(character)

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
    return {NAME_KEY: character_name, X_COORD_KEY: 0, Y_COORD_KEY: 0, CURRENT_EGO_KEY: 100, MAX_EGO_KEY: 100,
            LEVEL_KEY: 1, EXP_KEY: 0}


def check_for_level_up(character):
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
        character[LEVEL_KEY] += 1
        character[CURRENT_EGO_KEY] = 100
        print(character)
    elif character[EXP_KEY] == 100:
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
        print(character)


def gain_exp(character):
    character[EXP_KEY] = character[EXP_KEY] + 50
    print("Correct! Here's 50 EXP to help you prepare for your finals.")
    print(character)
    check_for_level_up(character)


def lose_ego(character):
    character[CURRENT_EGO_KEY] = character[CURRENT_EGO_KEY] - 50
    print("Wrong! You lost 50 ego points. If you have no ego points left, you'll fail your final.")
    print(character)


def check_game_over(character):
    if character[CURRENT_EGO_KEY] == 0:
        print("Answering all those questions incorrectly killed your ego.")
        print_game_over()
        sys.exit()


def print_game_over():
    print(r"""

                                    ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
                                    ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
                                    ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
                                    ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
                                    ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
                                    ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
                            """)


def get_valid_mc_answer():
    answer = ""
    while answer not in POSSIBLE_MULTIPLE_CHOICE_ANSWERS:
        answer = input("Choose one of a, b, c, or d. Type your answer here:")
    return answer


def challenge_addition(character):
    print("Time for addition!")
    if character[LEVEL_KEY] == 1:
        print("What is 5 + 5?")
        print("a: 30")
        print("b: 16")
        print("c: 5")
        print("d: 10")
        answer = get_valid_mc_answer()
        return answer == "d"
    elif character[LEVEL_KEY] == 2:
        print("What is 36 + 17?")
        print("a: 54")
        print("b: 53")
        print("c: 52")
        print("d: 56")
        answer = get_valid_mc_answer()
        return answer == "b"


def challenge_subtraction(character):
    print("Time for subtraction!")
    if character[LEVEL_KEY] == 1:
        print("What is 12 - 5?")
        print("a: 4")
        print("b: 7")
        print("c: 9")
        print("d: 10")
        answer = get_valid_mc_answer()
        return answer == "b"
    elif character[LEVEL_KEY] == 2:
        print("What is 67 - 28?")
        print("a: 51")
        print("b: 36")
        print("c: 39")
        print("d: 42")
        answer = get_valid_mc_answer()
        return answer == "c"


def challenge_multiplication(character):
    print("Time for multiplication!")
    if character[LEVEL_KEY] == 1:
        print("What is 12 x 11?")
        print("a: 132")
        print("b: 126")
        print("c: 151")
        print("d: 143")
        answer = get_valid_mc_answer()
        return answer == "a"
    elif character[LEVEL_KEY] == 2:
        print("What is 123 x 321?")
        print("a: 20,342")
        print("b: 17,196")
        print("c: 37,488")
        print("d: 39,483")
        answer = get_valid_mc_answer()
        return answer == "d"


def challenge_division(character):
    print("Time for division!")
    if character[LEVEL_KEY] == 1:
        print("What is 54 / 9?")
        print("a: 6")
        print("b: 7")
        print("c: 8")
        print("d: 9")
        answer = get_valid_mc_answer()
        return answer == "a"
    elif character[LEVEL_KEY] == 2:
        print("What is 686 / 98?")
        print("a: 15")
        print("b: 12")
        print("c: 7")
        print("d: 9")
        answer = get_valid_mc_answer()
        return answer == "c"


def challenge_derivatives(character):
    print("Time for derivatives!")
    if character[LEVEL_KEY] == 1:
        print("What is the derivative of y = 5x - 4?")
        print("a: 5")
        print("b: 6")
        print("c: 7")
        print("d: 8")
        answer = get_valid_mc_answer()
        return answer == "a"
    elif character[LEVEL_KEY] == 2:
        print("What is the derivative of (x + 2)^2 - 5x^3?")
        print("a: 12x - 3")
        print("b: -30x^2 + 4x - 6")
        print("c: 10x^2 + 5")
        print("d: -15x^2 + 2x + 4.")
        answer = get_valid_mc_answer()
        return answer == "d"


def challenge_integrals(character):
    print("Time for integrals!")
    if character[LEVEL_KEY] == 1:
        print("What is the integral of sinx?")
        print("a: sinx + C")
        print("b: −sinx + C")
        print("c: cosx + C")
        print("d: −cosx + C")
        answer = get_valid_mc_answer()
        return answer == "d"
    elif character[LEVEL_KEY] == 2:
        print("What is the integral of xsinx dx?")
        print("a: xcosx + sinx + c")
        print("b: xcosx - sinx + c")
        print("c: −xcosx + sinx + c")
        print("d: xcosx + sinx + c")
        answer = get_valid_mc_answer()
        return answer == "c"


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
    did_pass_challenge = CLASSES["Addition"](character)
    if did_pass_challenge:
        gain_exp(character)
    else:
        lose_ego(character)


def main():
    game()


if __name__ == "__main__":
    main()
