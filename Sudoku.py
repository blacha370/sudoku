from BoardGenerator import BoardGenerator
from SudokuSolver import SudokuSolver
from BoardGenerator import BoardGenerator
from copy import deepcopy


class Sudoku():
    def __init__(self, digits):
        self.digits = digits
        self.board = BoardGenerator.generateBoard(digits)
        self.cells_to_do = SudokuSolver.cells_to_solve(self.board)
        self.done_board = SudokuSolver.solve_board(
            deepcopy(self.board), self.cells_to_do)
