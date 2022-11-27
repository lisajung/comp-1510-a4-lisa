"""
Lisa Jung
A01332998
"""
def game(): # called from main
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
                           "prepare for finals! \n\nPlease write your name on this nametag *give you nametag* : " )
    return {NAME_KEY: character_name, X_COORD_KEY: 0, Y_COORD_KEY: 0, CURRENT_EGO_KEY: 100, MAX_EGO_KEY: 100}
print(make_character())




def main():
    pass


if __name__ == "__main__":
    main()


