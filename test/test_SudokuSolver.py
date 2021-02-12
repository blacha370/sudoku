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


class TestGetRow(TestCase):
    def test_get_row(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertEqual(SudokuSolver.get_row(board, 0), board[0:9])

        self.assertEqual(SudokuSolver.get_row(board, 1), board[0:9])

        self.assertEqual(SudokuSolver.get_row(board, 9), board[9:18])

        self.assertEqual(SudokuSolver.get_row(board, 17), board[9:18])

        self.assertEqual(SudokuSolver.get_row(board, 80), board[72:81])

    def test_get_row_with_negative_index(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_row, board, -1)

    def test_get_row_with_to_big_index(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_row, board, 81)

        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_row, board, 100)

    def test_get_row_with_not_int_as_position(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])

        self.assertRaises(TypeError, SudokuSolver.get_row, board, '1')

        self.assertRaises(TypeError, SudokuSolver.get_row, board, ' ')

        self.assertRaises(TypeError, SudokuSolver.get_row, board, '\n')

        self.assertRaises(TypeError, SudokuSolver.get_row, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.get_row, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.get_row, board, list())

        self.assertRaises(TypeError, SudokuSolver.get_row, board, dict())

        self.assertRaises(TypeError, SudokuSolver.get_row, board, tuple())

        self.assertRaises(TypeError, SudokuSolver.get_row, board, set())

        self.assertRaises(TypeError, SudokuSolver.get_row, board, -1.1)

        self.assertRaises(TypeError, SudokuSolver.get_row, board, True)

        self.assertRaises(TypeError, SudokuSolver.get_row, board, False)

        self.assertRaises(TypeError, SudokuSolver.get_row, board, None)
