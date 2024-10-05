# MiniMax Alpha-Beta Pruning

class MiniMax2:
    # Constructor
    def __init__(self, board):
        self.board = board

    # Method that checks available moves
    def availableMoves(self):
        moves = []
        for spot in range(9):
            if self.board.board[spot] == ' ':
                moves.append(spot)
        return moves

    # Method that gets the best move
    def getBestMove(self, AI):
        bestMove = None

        # If it's the AI's turn get the highest score, otherwise get the lowest score
        if AI:
            bestScore = -2

            # Go through all moves
            for move in self.availableMoves():
                # Check score and un-do move
                self.board.place(move, 'X')
                score = self.miniMax(False)
                self.board.place(move, ' ')

                # If the score is 1 (meaning it's already a MAX move), automatically return it
                if score == 1:
                    return move

                # If score is greater, save this as the best move and score
                if score > bestScore:
                    bestScore = score
                    bestMove = move
        else:
            bestScore = 2

            # Go through all moves
            for move in self.availableMoves():
                # Check score and un-do move
                self.board.place(move, 'O')
                score = self.miniMax(True)
                self.board.place(move, ' ')

                # If the score is -1 (meaning it's already a MIN move), automatically return it
                if score == -1:
                    return move

                # If score is lower, save this as the best move and score
                if score < bestScore:
                    bestScore = score
                    bestMove = move
        return bestMove

    # Recursive method that checks score
    def miniMax(self, maximizing):
        state = self.board.state()

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
                self.board.place(move, 'X')
                score = self.miniMax(False)
                self.board.place(move, ' ')

                # If the score is -1 (meaning it's already a MAX move), automatically return it
                if score == 1:
                    return 1

                # If score is greater, save it as the best score
                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                # Check score, un-do move, and save best score
                self.board.place(move, 'O')
                score = self.miniMax(True)
                self.board.place(move, ' ')

                # If the score is -1 (meaning it's already a MIN move), automatically return it
                if score == -1:
                    return -1

                # If score is greater, save it as the best score
                bestScore = min(bestScore, score)

        return bestScore
