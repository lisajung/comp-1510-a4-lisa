"""
Lisa Jung
A01332998
"""
import random


def game():  # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieved_goal = False
    # while not achieved_goal:
    #     // Tell the user where they are
    #     describe_current_location(board, character)
    #     direction = get_user_choice( )
    #     valid_move = validate_move(board, character, direction)
    #     if valid_move:
    #         move_character(character)
    #         describe_current_location(board, character)
    #         there_is_a_challenge = check_for_challenges()
    #         if there_is_a_challenge:
    #             execute_challenge_protocol(character)
    #             if character_has_leveled():
    #                 execute_glow_up_protocol()
    #         achieved_goal = check_if_goal_attained(board, character)
    #     else:
    #         // Tell the user they can’t go in that direction
    #         // Print end of game stuff like congratulations or sorry you died


NAME_KEY = "Name"
X_COORD_KEY = "X-coordinate"
Y_COORD_KEY = "Y-coordinate"
CURRENT_EGO_KEY = "Current Ego"
MAX_EGO_KEY = "Max Ego"


def make_character():
    character_name = input("Oh hey....buddy...welcome to finals season! "
                           "We've placed study sessions in classrooms \nthroughout the school for you to "
                           "prepare for finals! \n\nPlease write your name on this nametag *give you nametag* : ")
    return {NAME_KEY: character_name, X_COORD_KEY: 0, Y_COORD_KEY: 0, CURRENT_EGO_KEY: 100, MAX_EGO_KEY: 100}


def challenge_addition():
    print("Time for addition!")


def challenge_subtraction():
    print("Time for addition!")


def challenge_multiplication():
    print("Time for addition!")


def challenge_division():
    print("Time for addition!")


def challenge_derivatives():
    print("Time for addition!")


def challenge_integrals():
    print("Time for addition!")


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
    classroom_locations = random.sample(possible_locations, len(CLASSES))
    print(classroom_locations)
    board = {}
    # Populate an "empty room" board with the keys being the location and the value being the description.
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = "empty room"
    print(board)
    # Replace all locations that have a class with the given class's description
    class_descriptions = list(CLASSES.keys())
    for index in range(len(classroom_locations)):
        board[classroom_locations[index]] = class_descriptions[index]
    print(board)


make_board(5, 5)


def main():
    pass


if __name__ == "__main__":
    main()
