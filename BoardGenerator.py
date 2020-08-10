from SudokuSolver import SudokuSolver
from random import shuffle, randrange


class BoardGenerator:
    @staticmethod
    def blankBoard():
        board = [[0
                  for _ in range(9)]
                 for _ in range(9)]
        return tuple(board)

    @staticmethod
    def generateBoard(amount_of_digits):
        board = BoardGenerator.blankBoard()
        to_do_cells = SudokuSolver.cells_to_solve(board)
        shuffle(to_do_cells)

        to_do_cells = to_do_cells[0:15]
        board = SudokuSolver.solve_board(board, to_do_cells)

        to_do_cells = SudokuSolver.cells_to_solve(board)
        board = SudokuSolver.solve_board(board, to_do_cells)

        done_cells = SudokuSolver.cells_to_solve(BoardGenerator.blankBoard())
        for _ in range(81 - amount_of_digits):
            position = done_cells[randrange(len(done_cells))]
            done_cells.remove(position)
            board[position[0]][position[1]] = 0
        return board
