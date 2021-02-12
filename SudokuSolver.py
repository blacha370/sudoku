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
        pass

    @staticmethod
    def check_position(board: str, position: int):
        pass

    @staticmethod
    def check_board(board: str):
        pass

    @staticmethod
    def find_unsolved_positions(board: str):
        pass

    @staticmethod
    def solve_cell(board: str, position: int):
        pass

    @staticmethod
    def solve_board(board: str):
        pass
