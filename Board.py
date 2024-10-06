# Board class

class Board:
    # Constructor that builds the board and sets it to empty
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # Function that returns the state of the board. Who won, or if the game is still continuing, or if it's a tie
    def state(self):
        # Loop through all winning positions
        for a, b, c in ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)):
            # Check if a position is found and if the index is not empty (meaning there is a winner)
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                # Return who won
                return self.board[a]

        # If no winner, check if the board is full, meaning it's a tie, or if the game is still on
        if ' ' not in self.board:
            return 'tie'
        return 'continue'
