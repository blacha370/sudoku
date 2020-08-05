from Board import SudokuBoard
from Sudoku import Sudoku
from copy import deepcopy
sudoku_board_example = (
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0])

sudoku = SudokuBoard(sudoku_board_example)
Sudoku = Sudoku()


def sudokuSolver(board):
    edited_board = deepcopy(board)
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                row = Sudoku.get_row((y, x), edited_board)
                column = Sudoku.get_column((y, x), edited_board)
                box = Sudoku.get_box((y, x), edited_board)
                print((x, y), row, column, box)
                i = 1
                while True:
                    print(i)
                    if i not in row and i not in column and i not in box:
                        edited_board[y][x] = i
                        break
                    elif i == 9:
                        edited_board[y][x] = "error"
                        break
                    else:
                        i += 1
            else:
                print('value')
    print(edited_board)


sudokuSolver(sudoku.board)
