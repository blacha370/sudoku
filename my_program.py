from Board import SudokuBoard

sudoku_board_example = (
    [i + 11 for i in range(9)],
    [i + 21 for i in range(9)],
    [i + 31 for i in range(9)],
    [i + 41 for i in range(9)],
    [i + 51 for i in range(9)],
    [i + 61 for i in range(9)],
    [i + 71 for i in range(9)],
    [i + 81 for i in range(9)],
    [i + 91 for i in range(9)])

sudoku = SudokuBoard(sudoku_board_example)

print(sudoku.board)
print(sudoku.get_row((3, 4)))
print(sudoku.get_column((3, 4)))
print(sudoku.get_box((1, 6)))
