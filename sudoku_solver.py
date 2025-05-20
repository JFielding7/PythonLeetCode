from typing import List
from functools import reduce
from operator import or_


FAIL = 0
BOX_LEN = 3
NUMS = BOX_LEN * BOX_LEN
CELLS = NUMS * NUMS
CELL_EXTRACTOR = (1 << NUMS) - 1
EMPTY_GRID = (1 << (CELLS * NUMS)) - 1
ROW_MARKER = reduce(or_, (1 << (i * NUMS) for i in range(NUMS)))
COL_MARKER = reduce(or_, (1 << (i * CELLS) for i in range(NUMS)))
BOX_ROW_MARKER = reduce(or_, (1 << (i * NUMS) for i in range(BOX_LEN)))
BOX_MARKER = reduce(or_, (BOX_ROW_MARKER << (i * CELLS) for i in range(BOX_LEN)))


def place_num(grid, cell, num):
    row = cell // NUMS
    col = cell % NUMS
    box_row = row // BOX_LEN * BOX_LEN
    box_col = col // BOX_LEN * BOX_LEN
    return ((grid & ~(ROW_MARKER << (row * CELLS + num)))
            & ~(COL_MARKER << (col * NUMS + num))
            & ~(BOX_MARKER << (box_row * CELLS + box_col * NUMS + num))
            & ~(CELL_EXTRACTOR << (cell * NUMS))) | (1 << (cell * NUMS + num))

def solve(grid, curr_cell):
    if curr_cell == CELLS:
        return grid
    cell = (grid >> (curr_cell * NUMS)) & CELL_EXTRACTOR
    if cell == FAIL:
        return FAIL

    for i in range(NUMS):
        if (cell >> i) & 1:
            attempt = solve(place_num(grid, curr_cell, i), curr_cell + 1)
            if attempt != FAIL:
                return attempt

    return FAIL

def get_bit_board(board):
    bit_board = EMPTY_GRID
    cell = 0

    for row in board:
        for num in row:
            if num != '.':
                bit_board = place_num(bit_board, cell, int(num) - 1)
            cell += 1

    return bit_board

def update_board(bit_board, board):
    for cell in range(CELLS):
        board[cell // NUMS][cell % NUMS] = str(((bit_board >> (cell * NUMS)) & CELL_EXTRACTOR).bit_length())

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        solution = solve(get_bit_board(board), 0)
        update_board(solution, board)


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
for row in board:
    print(row)
