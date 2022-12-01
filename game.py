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
    print(possible_locations)
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
    return board


make_board(5, 5)


def get_character_location(character):
    """
    Retreive the character's location on the board.
    :param character: a dictionary representing the character
    :return: a tuple representing the character's location
    """
    character_location = (character[X_COORD_KEY], character[Y_COORD_KEY])
    print(character_location)
    return character_location


def describe_current_location(board, character):
    """
    This function describes where the character is on the board.
    :param board: a dictionary representing the game board
    :param character: a dictionary representing the character
    :return: a string describing the location
    """
    location_description = board[get_character_location(character)]
    print(location_description)
    return location_description


board = make_board(5, 5)
character = make_character()
describe_current_location(board, character)


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
    ask_which_direction = int(ask_which_direction)
    return ask_which_direction


def validate_move():
    location = get_character_location(character)
    direction_chosen = get_user_choice()
    if direction_chosen == 1:
        if location[0] == 0:
            print("There is no room in that direction. Let's choose another direction!")
            validate_move()
        else:
            new_location = list(get_character_location(character))
            new_location[0] -= 1
            print(new_location)
    if direction_chosen == 2:
        if location[1] == 4:
            print("There is no room in that direction. Let's choose another direction!")
            validate_move()
        else:
            new_location = list(get_character_location(character))
            new_location[1] += 1
            print(new_location)
    if direction_chosen == 3:
        if location[0] == 4:
            print("There is no room in that direction. Let's choose another direction!")
            validate_move()
        else:
            new_location = list(get_character_location(character))
            new_location[0] += 1
            print(new_location)
    if direction_chosen == 4:
        if location[1] == 0:
            print("There is no room in that direction. Let's choose another direction!")
            validate_move()
        else:
            new_location = list(get_character_location(character))
            new_location[1] -= 1
            print(new_location)







validate_move()


def main():
    pass


if __name__ == "__main__":
    main()
