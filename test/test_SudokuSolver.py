from unittest import TestCase
from sudoku.SudokuSolver import SudokuSolver
import random


class TestValidateBoard(TestCase):
    def test_validate_correct_board(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertTrue(SudokuSolver.validate_board(board))

    def test_validate_to_long_board(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(82)])
        self.assertFalse(SudokuSolver.validate_board(board))

        board = ''.join([str(random.randint(0, 9)) for _ in range(100)])
        self.assertFalse(SudokuSolver.validate_board(board))

    def test_validate_to_short_board(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(80)])
        self.assertFalse(SudokuSolver.validate_board(board))

        board = ''.join([str(random.randint(0, 9)) for _ in range(20)])
        self.assertFalse(SudokuSolver.validate_board(board))

    def test_validate_with_other_symbol_in_board(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(80)]) + 'a'
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = ''.join([str(random.randint(0, 9)) for _ in range(80)]) + '!'
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = ''.join([str(random.randint(0, 9)) for _ in range(80)]) + '/'
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = ''.join([str(random.randint(0, 9)) for _ in range(80)]) + '\n'
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = ''.join([str(random.randint(0, 9)) for _ in range(80)]) + ' '
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

    def test_validate_with_board_not_as_string(self):
        board = int(''.join([str(random.randint(0, 9)) for _ in range(81)]))
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = float(''.join([str(random.randint(0, 9)) for _ in range(79)]) + '0.1')
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = [str(random.randint(0, 9)) for _ in range(81)]
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = tuple([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = set([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = dict()
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = True
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = False
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = None
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)
