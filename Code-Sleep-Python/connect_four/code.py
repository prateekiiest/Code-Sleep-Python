import numpy as np
import math
import pygame
import sys

NB_COL = 7
NB_ROW = 6
BLUE = (0, 0, 255)  # RGB value
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


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


def draw_board(board):
    for c in range(NB_COL):
        for r in range(NB_ROW):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+1.5*SQUARESIZE)), RADIUS)

    for c in range(NB_COL):
        for r in range(NB_ROW):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
               pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()


board = make_board()
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100  # in pixels

width = NB_COL*SQUARESIZE
height = (NB_ROW+1)*SQUARESIZE  # extra row for piece

size = (width, height)
RADIUS = int(SQUARESIZE/2-5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont('monospace', 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (pos_x, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (pos_x, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            if turn is 0:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x/SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    # Adds winning condition
                    if winning_move(board, 1):
                        label = myfont.render('player 1 wins!', 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
    # ask for player 2 input
            else:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x/SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        label = myfont.render('player 2 wins!', 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
            draw_board(board)
            turn += 1
            turn = turn % 2  # resets turn to zero to allow player 1 to go

            if game_over:
                pygame.time.wait(3000)

