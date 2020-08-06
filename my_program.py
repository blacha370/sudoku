from Board import SudokuBoard
from Sudoku import Sudoku
from pprint import pprint

sudoku_board_example = (
    [1, 0, 7, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 2, 1],
    [0, 0, 0, 0, 0, 7, 9, 0, 5],
    [4, 0, 0, 0, 0, 1, 0, 6, 0],
    [0, 5, 0, 2, 0, 9, 0, 0, 3],
    [0, 8, 1, 0, 0, 4, 0, 0, 0],
    [0, 4, 3, 0, 5, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 5, 0])

sudoku = SudokuBoard(sudoku_board_example)
Sudoku = Sudoku()


def sudokuSolver(board):
    to_do_cells = []
    done_cells = []
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                to_do_cells.append((y, x))
    while len(to_do_cells) > 0:
        current_cell = to_do_cells[0]
        result = Sudoku.solve_cell(board, current_cell)
        if result:
            board[current_cell[0]][current_cell[1]] = result
            done_cells.append(to_do_cells.pop(0))
        else:
            board[current_cell[0]][current_cell[1]] = 0
            to_do_cells.insert(0, done_cells.pop())
    pprint(board)


sudokuSolver(sudoku.board)
