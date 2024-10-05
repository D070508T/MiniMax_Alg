# MiniMax Transposition Tables

class MiniMax4:
    # Constructor
    def __init__(self, board):
        self.board = board
        self.tables = {}    # Transposition tables

    # Method that checks available moves
    def availableMoves(self):
        moves = []
        for spot in range(9):
            if self.board.board[spot] == ' ':
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
                self.board.place(move, 'X')
                score = self.miniMax(False)
                self.board.place(move, ' ')

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

                # If score is lower, save this as the best move and score
                if score < bestScore:
                    bestScore = score
                    bestMove = move

        return bestMove

    # Recursive method that checks score
    def miniMax(self, maximizing):
        # If the board has already been calculated, return the previous result
        if self.board.board in self.tables:
            return self.tables[self.board.board]

        state = self.board.state()

        # If the game is over, return a value for the move and save the board
        if state == 'X':
            self.tables[self.board.board] = 1
            return 1
        elif state == 'O':
            self.tables[self.board.board] = -1
            return -1
        elif state == 'tie':
            self.tables[self.board.board] = 0
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
                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                # Check score, un-do move, and save best score
                self.board.place(move, 'O')
                score = self.miniMax(True)
                self.board.place(move, ' ')
                bestScore = min(bestScore, score)

        # Save the board and value
        self.tables[self.board.board] = bestScore
        return bestScore
