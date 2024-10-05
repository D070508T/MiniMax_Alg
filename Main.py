# Importing Libraries
import random
import time
from Board import Board
from MiniMax1 import MiniMax1
from MiniMax2 import MiniMax2
from MiniMax3 import MiniMax3
from MiniMax4 import MiniMax4
from MiniMax5 import MiniMax5
from MiniMax6 import MiniMax6
from MiniMax7 import MiniMax7
from MiniMax8 import MiniMax8

# Main Loop
while True:
    timeToChoose = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ver = input('Which version of MiniMax would you like to test (1-8): ')
    x = int(input('How many times would you like to run: '))

    start = time.perf_counter()
    for i in range(x):
        # Reset board and choose algorithm version
        board = Board()
        if ver == '1':
            minimax = MiniMax1(board)
        elif ver == '2':
            minimax = MiniMax2(board)
        elif ver == '3':
            minimax = MiniMax3(board)
        elif ver == '4':
            minimax = MiniMax4(board)
        elif ver == '5':
            minimax = MiniMax5(board)
        elif ver == '6':
            minimax = MiniMax6(board)
        elif ver == '7':
            minimax = MiniMax7(board)
        else:
            minimax = MiniMax8(board)

        while board.state() == 'continue':
            # Count how many empty spots there are
            empty = board.board.count(' ')

            # Choose a move and record time
            startTime = time.perf_counter()
            move = minimax.getBestMove(False)
            timeToChoose[empty] += (time.perf_counter() - startTime) * 1000000

            # Choose a random move (player 2)
            while True:
                num = random.randint(0, 8)
                if board.board[num] == ' ':
                    board.place(num, 'O')
                    break

            # If the game isn't over, choose a move and record time
            if board.state() == 'continue':
                startTime = time.perf_counter()
                move = minimax.getBestMove(True)
                timeToChoose[empty - 1] += (time.perf_counter() - startTime) * 1000000

                board.place(move, 'X')

    # Record total time taken
    elapsed = time.perf_counter() - start

    # Display times for every move
    for i in range(10):
        print(f'Average time taken for {i} available move(s): {round(timeToChoose[i] / x, 7)} microseconds')

    # Display total time
    print(f'''time elapsed: {round(elapsed * 1000000, 7)} microseconds
time per run: {round(elapsed/x * 1000000, 7)}''')
