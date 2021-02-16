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


class TestGetColumn(TestCase):
    def test_get_column(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertEqual(SudokuSolver.get_column(board, 1), board[1::9])

        self.assertEqual(SudokuSolver.get_column(board, 9), board[0::9])

        self.assertEqual(SudokuSolver.get_column(board, 80), board[8::9])

    def test_get_column_with_negative_index(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_column, board, -1)

    def test_get_column_with_to_big_index(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_column, board, 81)

        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_column, board, 100)

    def test_get_column_with_not_int_as_position(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])

        self.assertRaises(TypeError, SudokuSolver.get_column, board, '1')

        self.assertRaises(TypeError, SudokuSolver.get_column, board, ' ')

        self.assertRaises(TypeError, SudokuSolver.get_column, board, '\n')

        self.assertRaises(TypeError, SudokuSolver.get_column, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.get_column, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.get_column, board, list())

        self.assertRaises(TypeError, SudokuSolver.get_column, board, dict())

        self.assertRaises(TypeError, SudokuSolver.get_column, board, tuple())

        self.assertRaises(TypeError, SudokuSolver.get_column, board, set())

        self.assertRaises(TypeError, SudokuSolver.get_column, board, -1.1)

        self.assertRaises(TypeError, SudokuSolver.get_column, board, True)

        self.assertRaises(TypeError, SudokuSolver.get_column, board, False)

        self.assertRaises(TypeError, SudokuSolver.get_column, board, None)


class TestGetBox(TestCase):
    def test_get_box(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertEqual(SudokuSolver.get_box(board, 1), board[0:3] + board[9:12] + board[18:21])

        self.assertEqual(SudokuSolver.get_box(board, 8), board[6:9] + board[15:18] + board[24:27])

        self.assertEqual(SudokuSolver.get_box(board, 80), board[60:63] + board[69:72] + board[78:81])

    def test_get_box_with_negative_index(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_box, board, -1)

    def test_get_box_with_to_big_index(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_box, board, 81)

        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])
        self.assertRaises(IndexError, SudokuSolver.get_box, board, 100)

    def test_get_box_with_not_int_as_position(self):
        board = ''.join([str(random.randint(0, 9)) for _ in range(81)])

        self.assertRaises(TypeError, SudokuSolver.get_box, board, '1')

        self.assertRaises(TypeError, SudokuSolver.get_box, board, ' ')

        self.assertRaises(TypeError, SudokuSolver.get_box, board, '\n')

        self.assertRaises(TypeError, SudokuSolver.get_box, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.get_box, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.get_box, board, list())

        self.assertRaises(TypeError, SudokuSolver.get_box, board, dict())

        self.assertRaises(TypeError, SudokuSolver.get_box, board, tuple())

        self.assertRaises(TypeError, SudokuSolver.get_box, board, set())

        self.assertRaises(TypeError, SudokuSolver.get_box, board, -1.1)

        self.assertRaises(TypeError, SudokuSolver.get_box, board, True)

        self.assertRaises(TypeError, SudokuSolver.get_box, board, False)

        self.assertRaises(TypeError, SudokuSolver.get_box, board, None)


class TestCheckPosition(TestCase):
    def test_check_board(self):
        board = '0' * 81
        self.assertTrue(SudokuSolver.check_position(board, 0))

        board = '1' * 81
        self.assertFalse(SudokuSolver.check_position(board, 1))

        board = '1' + '0' * 80
        self.assertTrue(SudokuSolver.check_position(board, 0))

        board = '123456678' + '0' * 72
        self.assertFalse(SudokuSolver.check_position(board, 0))

        board = '1230000004560000007890000001' + '0' * 53
        self.assertFalse(SudokuSolver.check_position(board, 0))

        board = '123000000456000000799' + '0' * 60
        self.assertFalse(SudokuSolver.check_position(board, 0))

    def test_check_board_with_too_big_position(self):
        board = '0' * 81
        self.assertRaises(IndexError, SudokuSolver.check_position, board, 81)

        self.assertRaises(IndexError, SudokuSolver.check_position, board, 100)

    def test_check_board_with_negative_index(self):
        board = '0' * 81
        self.assertRaises(IndexError, SudokuSolver.check_position, board, -1)

        self.assertRaises(IndexError, SudokuSolver.check_position, board, -19)

    def test_check_position_with_not_int_as_position(self):
        board = '0' * 81

        self.assertRaises(TypeError, SudokuSolver.check_position, board, '1')

        self.assertRaises(TypeError, SudokuSolver.check_position, board, ' ')

        self.assertRaises(TypeError, SudokuSolver.check_position, board, '\n')

        self.assertRaises(TypeError, SudokuSolver.check_position, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.check_position, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.check_position, board, list())

        self.assertRaises(TypeError, SudokuSolver.check_position, board, dict())

        self.assertRaises(TypeError, SudokuSolver.check_position, board, tuple())

        self.assertRaises(TypeError, SudokuSolver.check_position, board, set())

        self.assertRaises(TypeError, SudokuSolver.check_position, board, -1.1)

        self.assertRaises(TypeError, SudokuSolver.check_position, board, True)

        self.assertRaises(TypeError, SudokuSolver.check_position, board, False)

        self.assertRaises(TypeError, SudokuSolver.check_position, board, None)


class TestCheckBoard(TestCase):
    def test_check_board(self):
        board = '0' * 81
        self.assertTrue(SudokuSolver.check_board(board))

        board = '123456789456789123789123456214365897365897214897214365531642978642978531978531642'
        self.assertTrue(SudokuSolver.check_board(board))

        board = board[:80] + '3'
        self.assertFalse(SudokuSolver.check_board(board))

        board = '1' * 81
        self.assertFalse(SudokuSolver.check_board(board))
