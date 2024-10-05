class MiniMax4:
    def __init__(self, board):
        self.board = board
        self.tables = {}

    def availableMoves(self):
        moves = []
        for i in range(9):
            if self.board.board[i] == ' ':
                moves.append(i)
        return moves

    def getBestMove(self, AI):
        bestMove = None

        if AI:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False)
                self.board.place(move, ' ')

                if score > bestScore:
                    bestScore = score
                    bestMove = move
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True)
                self.board.place(move, ' ')

                if score < bestScore:
                    bestScore = score
                    bestMove = move
        return bestMove

    def miniMax(self, maximizing):
        if self.board.board in self.tables:
            return self.tables[self.board.board]

        state = self.board.state()

        if state == 'X':
            self.tables[self.board.board] = 1
            return 1
        elif state == 'O':
            self.tables[self.board.board] = -1
            return -1
        elif state == 'tie':
            self.tables[self.board.board] = 0
            return 0

        if maximizing:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False)
                self.board.place(move, ' ')
                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True)
                self.board.place(move, ' ')
                bestScore = min(bestScore, score)

        self.tables[self.board.board] = bestScore
        return bestScore
