import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Creates grid to be filled

NB_COL = 7
NB_ROW = 6


def make_board():
    board = np.zeros((NB_ROW, NB_COL))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[NB_ROW-1][col] == 0


def get_next_open_row(board, col):
    for r in range(NB_ROW):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(baord, piece):
    # Check hozizontal locations for win
    for c in range(NB_COL-3):
        for r in range(NB_ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Check verticle locations for win
    for c in range(NB_COL):
        for r in range(NB_ROW-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
   # check for positively sloped diags
    for c in range(NB_COL-3):
        for r in range(NB_ROW-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
   # check for negitively sloped diags
    for c in range(NB_COL-3):
        for r in range(3,NB_ROW):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = make_board()
game_over = False
turn = 0

print_board(board)
while not game_over:
    # ask player 1 input
    if turn is 0:
        col = int(input('Player 1 make your Selection (0-6):'))
    # ask for player 2 input
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            # Adds winning condition
            if winning_move(board, 1):
               print('player 1 wins!')
               game_over = True
               print_board(board)
               break
    else:
        col = int(input('Player 2 make your Selection (0-6):'))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if winning_move(board, 2):
               print('player 2 wins!')
               game_over = True
               print_board(board)
               break

    print_board(board)
    turn += 1
    turn = turn % 2  # resets turn to zero to allow player 1 to go
