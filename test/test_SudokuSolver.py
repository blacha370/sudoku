from unittest import TestCase
from sudoku.SudokuSolver import SudokuSolver, BoardError
import random


class TestValidateBoard(TestCase):
    def test_validate_correct_board(self):
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertTrue(SudokuSolver.validate_board(board))

    def test_validate_to_long_board(self):
        board = [random.randint(0, 9) for _ in range(82)]
        self.assertFalse(SudokuSolver.validate_board(board))

        board = [random.randint(0, 9) for _ in range(100)]
        self.assertFalse(SudokuSolver.validate_board(board))

    def test_validate_to_short_board(self):
        board = [random.randint(0, 9) for _ in range(80)]
        self.assertFalse(SudokuSolver.validate_board(board))

        board = [random.randint(0, 9) for _ in range(20)]
        self.assertFalse(SudokuSolver.validate_board(board))

    def test_validate_with_wrong_number_in_board(self):
        board = [random.randint(0, 9) for _ in range(80)]
        board.append(10)
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(-1)
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

    def test_validate_with_wrong_data_inside_board(self):
        board = [random.randint(0, 9) for _ in range(80)]
        board.append(1.1)
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(-1.1)
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append('')
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append('0')
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append('1')
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append('-1')
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(list())
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(tuple())
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(set())
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(dict())
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(True)
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(False)
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

        board = [random.randint(0, 9) for _ in range(80)]
        board.append(None)
        self.assertRaises(ValueError, SudokuSolver.validate_board, board)

    def test_validate_with_board_not_as_list(self):
        board = 1234
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = 1234.1
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = '123'
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = tuple()
        self.assertRaises(TypeError, SudokuSolver.validate_board, board)

        board = set()
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
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertEqual(SudokuSolver.get_row(board, 0), board[0:9])

        self.assertEqual(SudokuSolver.get_row(board, 1), board[0:9])

        self.assertEqual(SudokuSolver.get_row(board, 9), board[9:18])

        self.assertEqual(SudokuSolver.get_row(board, 17), board[9:18])

        self.assertEqual(SudokuSolver.get_row(board, 80), board[72:81])

    def test_get_row_with_negative_index(self):
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.get_row, board, -1)

    def test_get_row_with_to_big_index(self):
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.get_row, board, 81)

        self.assertRaises(IndexError, SudokuSolver.get_row, board, 100)

    def test_get_row_with_not_int_as_position(self):
        board = [random.randint(0, 9) for _ in range(81)]

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
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertEqual(SudokuSolver.get_column(board, 1), board[1::9])

        self.assertEqual(SudokuSolver.get_column(board, 9), board[0::9])

        self.assertEqual(SudokuSolver.get_column(board, 80), board[8::9])

    def test_get_column_with_negative_index(self):
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.get_column, board, -1)

    def test_get_column_with_to_big_index(self):
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.get_column, board, 81)

        self.assertRaises(IndexError, SudokuSolver.get_column, board, 100)

    def test_get_column_with_not_int_as_position(self):
        board = [random.randint(0, 9) for _ in range(81)]

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
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertEqual(SudokuSolver.get_box(board, 1), board[0:3] + board[9:12] + board[18:21])

        self.assertEqual(SudokuSolver.get_box(board, 8), board[6:9] + board[15:18] + board[24:27])

        self.assertEqual(SudokuSolver.get_box(board, 80), board[60:63] + board[69:72] + board[78:81])

    def test_get_box_with_negative_index(self):
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.get_box, board, -1)

    def test_get_box_with_to_big_index(self):
        board = [random.randint(0, 9) for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.get_box, board, 81)

        self.assertRaises(IndexError, SudokuSolver.get_box, board, 100)

    def test_get_box_with_not_int_as_position(self):
        board = [random.randint(0, 9) for _ in range(81)]

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
        board = [0 for _ in range(81)]
        self.assertTrue(SudokuSolver.check_position(board, 0))

        board = [1 for _ in range(81)]
        self.assertFalse(SudokuSolver.check_position(board, 1))

        board = [0 for _ in range(81)]
        board.append(1)
        self.assertTrue(SudokuSolver.check_position(board, 0))

        board = [0 for _ in range(81)]
        board[0] = 1
        board[2] = 1
        self.assertFalse(SudokuSolver.check_position(board, 0))

        board = [0 for _ in range(81)]
        board[0] = 1
        board[9] = 1
        self.assertFalse(SudokuSolver.check_position(board, 0))

        board = [0 for _ in range(81)]
        board[0] = 1
        board[10] = 1
        self.assertFalse(SudokuSolver.check_position(board, 0))

    def test_check_board_with_too_big_position(self):
        board = [0 for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.check_position, board, 81)

        self.assertRaises(IndexError, SudokuSolver.check_position, board, 100)

    def test_check_board_with_negative_index(self):
        board = [0 for _ in range(81)]
        self.assertRaises(IndexError, SudokuSolver.check_position, board, -1)

        self.assertRaises(IndexError, SudokuSolver.check_position, board, -19)

    def test_check_position_with_not_int_as_position(self):
        board = [0 for _ in range(81)]

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
        board = [0 for _ in range(81)]
        self.assertTrue(SudokuSolver.check_board(board))

        board = '123456789456789123789123456214365897365897214897214365531642978642978531978531642'
        board = [int(i) for i in board]
        self.assertTrue(SudokuSolver.check_board(board))

        board[80] = 3
        self.assertFalse(SudokuSolver.check_board(board))

        board = [1 for _ in range(81)]
        self.assertFalse(SudokuSolver.check_board(board))


class TestFindUnsolvedPositions(TestCase):
    def test_find_unsolved_positions(self):
        board = [0 for _ in range(81)]
        self.assertEqual(SudokuSolver.find_unsolved_positions(board), list(range(81)))

        board = '123456789456789123789123456214365897365897214897214365531642978642978531978531642'
        board = [int(i) for i in board]
        self.assertEqual(SudokuSolver.find_unsolved_positions(board), [])

        board[80] = 0
        self.assertEqual(SudokuSolver.find_unsolved_positions(board), [80])


class TestSolveCell(TestCase):
    def test_solve_cell(self):
        board = '123456789456789123789123456214365897365897214897214365531642978642978531978531640'
        board = [int(i) for i in board]
        result = SudokuSolver.solve_cell(board, 80)
        self.assertTrue(result[0])
        self.assertEqual(result[1], board[:80] + [2])

        board = [0 for _ in board]
        result = SudokuSolver.solve_cell(board, 0)
        self.assertTrue(result[0])
        self.assertEqual(result[1], [1] + board[1:])

        result = SudokuSolver.solve_cell(board, 1)
        self.assertTrue(result[0])
        self.assertEqual(result[1], [0, 1] + board[2:])

        board = [1] + [0 for _ in range(80)]
        result = SudokuSolver.solve_cell(board, 1)
        self.assertTrue(result[0])
        self.assertEqual(result[1], [1, 2] + board[2:])

    def test_solve_cell_that_should_be_false(self):
        board = '123456789456789123789123456214365897365897214897214365531642978642978531978531642'
        board = [int(i) for i in board]
        result = SudokuSolver.solve_cell(board, 0)
        self.assertFalse(result[0])
        self.assertEqual(result[1], [0] + board[1:])

        board = '0123456789' + '0' * 71
        board = [int(i) for i in board]
        result = SudokuSolver.solve_cell(board, 0)
        self.assertFalse(result[0])
        self.assertEqual(result[1], board)

    def test_solve_cell_with_not_int_as_position(self):
        board = [0 for _ in range(81)]

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, '1')

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, ' ')

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, '\n')

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, 1.1)

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, list())

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, dict())

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, tuple())

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, set())

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, -1.1)

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, True)

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, False)

        self.assertRaises(TypeError, SudokuSolver.solve_cell, board, None)


class TestSolveBoard(TestCase):
    def test_solve_board(self):
        board = '0' * 81
        board = [int(i) for i in board]
        result = SudokuSolver.solve_board(board)
        self.assertEqual(result, [int(i) for i in
                                  '123456789456789123789123456214365897365897214897214365531642978642978531978531642'])

        board = '000090020520700460800600030000800370200431005083007000030009008051008093040010000'
        board = [int(i) for i in board]
        result = SudokuSolver.solve_board(board)
        self.assertEqual(result, [int(i) for i in
                                  '364195827529783461817624539195862374276431985483957216632579148751248693948316752'])

    def test_solve_unsolvable_board(self):
        board = '11' + '0' * 79
        board = [int(i) for i in board]
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = [0 for _ in range(80)]
        board.append('*')
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = [0 for _ in range(80)]
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = [0 for _ in range(82)]
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

    def test_solve_board_with_not_string_as_board(self):
        board = 1234
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = 1234.1
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = '123'
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = tuple()
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = set()
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = dict()
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = True
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = False
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)

        board = None
        self.assertRaises(BoardError, SudokuSolver.solve_board, board)