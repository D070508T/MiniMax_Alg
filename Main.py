# Importing Libraries
import random
import time
from Board import Board
from MiniMax1 import MiniMax1
from MiniMax2 import MiniMax2
from MiniMax3 import MiniMax3
from MiniMax4 import MiniMax4

# Main Loop
while True:
    timeToChoose = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ver = input('Which version of MiniMax would you like to test (1-5): ')
    x = int(input('How many times would you like to run: '))

    start = time.perf_counter()
    for i in range(x):
        board = Board()
        if ver == '1':
            minimax = MiniMax1(board)
        elif ver == '2':
            minimax = MiniMax2(board)
        elif ver == '3':
            minimax = MiniMax3(board)
        else:
            minimax = MiniMax4(board)

        while board.state() == 'continue':
            empty = 0
            for j in range(9):
                if board.board[j] == ' ':
                    empty += 1

            startTime = time.perf_counter()
            move = minimax.getBestMove(False)
            timeToChoose[empty] += (time.perf_counter() - startTime) * 1000000

            while True:
                num = random.randint(0, 8)
                if board.board[num] == ' ':
                    break

            board.place(num, 'O')

            if board.state() == 'continue':
                startTime = time.perf_counter()
                move = minimax.getBestMove(True)
                timeToChoose[empty - 1] += (time.perf_counter() - startTime) * 1000000

                board.place(move, 'X')

    elapsed = time.perf_counter() - start

    for i in range(10):
        print(f'Average time taken for {i} available move(s): {round(timeToChoose[i] / x, 7)} microseconds')

    total = 0
    for call in timeToChoose:
        total += call

    print(f'time elapsed: {round(elapsed * 1000000, 7)} microseconds')
