class MiniMax3:
    def __init__(self, board):
        self.board = board

    def availableMoves(self):
        moves = []
        for i in (4, 0, 2, 6, 8, 1, 3, 5, 7):
            if self.board.board[i] == ' ':
                moves.append(i)
        return moves

    def getBestMove(self, AI):
        bestMove = None

        if AI:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False, 4)
                self.board.place(move, ' ')

                if score > bestScore:
                    bestScore = score
                    bestMove = move
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True, 4)
                self.board.place(move, ' ')

                if score < bestScore:
                    bestScore = score
                    bestMove = move
        return bestMove

    def miniMax(self, maximizing, limit):
        state = self.board.state()

        if state == 'X':
            return 1
        elif state == 'O':
            return -1
        elif state == 'tie' or limit == 0:
            return 0

        if maximizing:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False, limit-1)
                self.board.place(move, ' ')
                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True, limit-1)
                self.board.place(move, ' ')
                bestScore = min(bestScore, score)

        return bestScore
