'''
SI 507 Fall 2018 Homework 1
'''

## Tic-Tac-Toe under development by Gui Ruggiero

# Create board - Setup the data structure for storing board data
    
board_data = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

# Boolean variable to flag when the game is over
game_ended = False

# Variable to identify which player plays next - X is 0, O is 1
user_turn = 0

# Loop until game is over

while game_ended == False:

    # Step 1: Print board
    '''
    - This function will take in current board data and print out the board in the console as shown 
    in the instructions
    - parameter: board_data - a data structure used for holding current moves on the board
    - return: none
    '''

    def print_board(board_data):
        
        print(" ", board_data[0][0], " | ", board_data[0][1], " | ", board_data[0][2])
        print("-----------")
        print(" ", board_data[1][0], " | ", board_data[1][1], " | ", board_data[1][2])
        print("-----------")
        print(" ", board_data[2][0], " | ", board_data[2][1], " | ", board_data[2][2])

    # Step 2: Requests and translates play
    '''
    - This function will check who plays next via the variable user_turn, ask for the input
    of the play on a specific format (C, NE, SW etc) stored under play_human, and translate
    it to the format [i,j] stored in play_machine
    - parameter: play_human - string from the user as one of the following: NW, N, NE, W, C,
    E, SW, S, SE
    - return: play_machine - a list of the play in the translated [i,j] format
    '''

    def get_translate_play(play_human)
        pass

    # Step 3: Validates play
    '''
    - This function will validate if the desired play will be accepted, which means checking
    if play_human is one of the 9 options and if the picked position is empty. If yes and yes,
    user_turn is updated and program continues; else, player gets a warning and is asked to
    pick another position by calling get_play again
    - parameter: play_machine - a list of the play in the translated [i,j] format
    - return: play_machine - updated with translated and validated play
    '''

    def validate_play(play_machine)
        pass

    # Step 4: Consolidates play
    '''
    - This function will take the translated and validated play and update board_data accordingly
    - parameter: play_machine - updated with translated and validated play
    - return: board_data - updated board data
    '''

    def store_play(play_machine)
        pass

    # Step 5: Determine if game is over
    '''
    - Take in the current board data and determine if one player wins the game, if the game draws,
    or if the game continues. If the game is over, update game_ended to terminate the loop and
    print the result; else, program (loop) continues.
    - parameter: board_data - updated board data
    - return: game_ended - information about current game status
    '''

    def determine_over(board_data):
        pass