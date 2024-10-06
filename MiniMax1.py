# MiniMax Base Version

from util import board_state


class MiniMax1:
    # Constructor
    def __init__(self, board):
        self.board = board

    # Method that checks available moves
    def availableMoves(self):
        moves = []
        for spot in range(9):
            if self.board[spot] == ' ':
                moves.append(spot)
        return moves

    # Method that gets best move
    def getBestMove(self, AI):
        bestMove = None

        # If it's the AI's turn get the highest score, otherwise get the lowest score
        if AI:
            bestScore = -2

            # Go through all moves
            for move in self.availableMoves():
                # Check score and un-do move
                self.board[move] = 'X'
                score = self.miniMax(False)
                self.board[move] = ' '

                # If score is greater, save this as the best move and score
                if score > bestScore:
                    bestScore = score
                    bestMove = move
        else:
            bestScore = 2

            # Go through all moves
            for move in self.availableMoves():

                # Check score and un-do move
                self.board[move] = 'O'
                score = self.miniMax(True)
                self.board[move] = ' '

                # If score is lower, save this as the best move and score
                if score < bestScore:
                    bestScore = score
                    bestMove = move

        return bestMove

    # Recursive method that checks score
    def miniMax(self, maximizing):
        state = board_state(self.board)

        # If the game is over, return a value for the move
        if state == 'X':
            return 1
        elif state == 'O':
            return -1
        elif state == 'tie':
            return 0

        # If it's the AI's turn get the highest score, otherwise get the lowest score
        if maximizing:
            bestScore = -2

            # Go through all moves
            for move in self.availableMoves():
                # Check score, un-do move, and save best score
                self.board[move] = 'X'
                score = self.miniMax(False)
                self.board[move] = ' '
                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                # Check score, un-do move, and save best score
                self.board[move] = 'O'
                score = self.miniMax(True)
                self.board[move] = ' '
                bestScore = min(bestScore, score)

        return bestScore
