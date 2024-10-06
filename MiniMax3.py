# MiniMax Depth Limit and Move Order

from util import board_state


class MiniMax3:
    # Constructor
    def __init__(self, board):
        self.board = board

    # Method that checks for available moves in the right order
    def availableMoves(self):
        moves = []
        for i in (4, 0, 2, 6, 8, 1, 3, 5, 7):
            if self.board[i] == ' ':
                moves.append(i)
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
                score = self.miniMax(False, 4)    # With limit 4
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
                score = self.miniMax(True, 4)    # With limit 4
                self.board[move] = ' '

                # If score is lower, save this as the best move and score
                if score < bestScore:
                    bestScore = score
                    bestMove = move

        return bestMove

    # Recursive method that checks score with limit
    def miniMax(self, maximizing, limit):
        state = board_state(self.board)

        # If the game is over, return a value for the move
        if state == 'X':
            return 1
        elif state == 'O':
            return -1
        elif state == 'tie' or limit == 0:
            return 0

        # If it's the AI's turn get the highest score, otherwise get the lowest score
        if maximizing:
            bestScore = -2

            # Go through all moves
            for move in self.availableMoves():
                # Check score, un-do move, and save best score
                self.board[move] = 'X'
                score = self.miniMax(False, limit-1)    # Lower limit by 1
                self.board[move] = ' '
                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                # Check score, un-do move, and save best score
                self.board[move] = 'O'
                score = self.miniMax(False, limit-1)    # Lower limit by 1
                self.board[move] = ' '
                bestScore = min(bestScore, score)

        return bestScore
