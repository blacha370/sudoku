class BoardError(Exception):
    pass


class SudokuSolver:
    @staticmethod
    def validate_board(board: str):
        if not isinstance(board, str):
            raise TypeError
        for char in board:
            int(char)  # check if board contains only digits
        if len(board) == 81:
            return True
        else:
            return False

    @staticmethod
    def get_row(board: str, position: int):
        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError
        elif not 0 <= position <= 80:
            raise IndexError
        else:
            borders = ((position // 9) * 9, (position // 9 + 1) * 9)
            return board[borders[0]:borders[1]]

    @staticmethod
    def get_column(board: str, position: int):
        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError
        elif not 0 <= position <= 80:
            raise IndexError
        else:
            return board[position % 9::9]

    @staticmethod
    def get_box(board: str, position: int):
        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError
        elif not 0 <= position <= 80:
            raise IndexError
        else:
            max_index = (position // 27 + 1) * 27
            box_rows = board[max_index - 27:max_index]
            box_index = position % 27 % 9 // 3
            box = ''.join([box_rows[3 * box_index + 9 * i:3 * (box_index + 1) + 9 * i] for i in range(3)])
            return box

    @staticmethod
    def check_position(board: str, position: int):
        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError
        elif not 0 <= position <= 80:
            raise IndexError
        else:
            row = SudokuSolver.get_row(board, position).replace('0', '')
            column = SudokuSolver.get_column(board, position).replace('0', '')
            box = SudokuSolver.get_box(board, position).replace('0', '')
            if len(row) == len(set(row)) and len(column) == len(set(column)) and len(box) == len(set(box)):
                return True
            else:
                return False

    @staticmethod
    def check_board(board: str):
        for i in range(3):
            for j in range(3):
                position = 12 * (j + 2 * i) + 4 * i
                if not SudokuSolver.check_position(board, position):
                    return False
        return True

    @staticmethod
    def find_unsolved_positions(board: str):
        unsolved_positions = []
        for index, number in enumerate(board):
            if number == '0':
                unsolved_positions.append(index)
        return unsolved_positions

    @staticmethod
    def solve_cell(board: str, position: int):
        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError
        elif not 0 <= position <= 80:
            raise IndexError
        else:
            used_numbers = SudokuSolver.get_row(board, position) + SudokuSolver.get_column(board, position) + SudokuSolver.get_box(board, position)
            available_numbers = [str(i) for i in range(int(board[position]) + 1, 10) if str(i) not in used_numbers]
            if len(available_numbers) > 0:
                return True, board[:position] + available_numbers[0] + board[position + 1:]
            else:
                return False, board[:position] + '0' + board[position + 1:]

    @staticmethod
    def solve_board(board: str):
        try:
            if not SudokuSolver.validate_board(board):
                raise BoardError('Board is too long or to short')
        except TypeError:
            raise BoardError('Board should be string instead of {0}'.format(type(board)))
        except ValueError:
            raise BoardError('Wrong symbol inside board, allowed symbols: 0-9)')
        if SudokuSolver.check_board(board):
            unsolved_positions = SudokuSolver.find_unsolved_positions(board)
            index = 0
            while SudokuSolver.find_unsolved_positions(board):
                is_cell_solved, board = SudokuSolver.solve_cell(board, unsolved_positions[index])
                if index == 0 and not is_cell_solved:
                    raise BoardError('Board is unsolvable')
                elif is_cell_solved:
                    index += 1
                else:
                    index -= 1
            return board
        else:
            raise BoardError('Board is unsolvable')
