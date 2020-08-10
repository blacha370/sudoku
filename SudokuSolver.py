class SudokuSolver:
    @staticmethod
    def get_row(position: tuple, board):
        return board[position[0]]

    @staticmethod
    def get_column(position: tuple, board):
        return [element[position[1]]
                for element in board]

    @staticmethod
    def get_horizontal_box_line(position, y, board):
        box = list()
        if position[1] <= 2:
            for x in range(3):
                box.append(board[y][x])
        elif position[1] <= 5:
            for x in range(3, 6):
                box.append(board[y][x])
        elif position[1] <= 8:
            for x in range(6, 9):
                box.append(board[y][x])
        else:
            return False
        return box

    @staticmethod
    def get_box(position, board):
        box = list()
        if position[0] <= 2:
            for y in range(3):
                for element in SudokuSolver.get_horizontal_box_line(position, y, board):
                    box.append(element)
        elif position[0] <= 5:
            for y in range(3, 6):
                for element in SudokuSolver.get_horizontal_box_line(position, y, board):
                    box.append(element)
        elif position[0] <= 8:
            for y in range(6, 9):
                for element in SudokuSolver.get_horizontal_box_line(position, y, board):
                    box.append(element)
        else:
            return False
        return box

    @staticmethod
    def solve_cell(board, position):
        usedNumbers = set()
        usedNumbers = usedNumbers | set(SudokuSolver.get_row(position, board))
        usedNumbers = usedNumbers | set(
            SudokuSolver.get_column(position, board))
        usedNumbers = usedNumbers | set(SudokuSolver.get_box(position, board))
        i = board[position[0]][position[1]] + 1
        while True:
            if i not in usedNumbers and i <= 9:
                return i
            elif i > 9:
                return False
            else:
                i += 1

    @staticmethod
    def cells_to_solve(board):
        to_do_cells = []
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    to_do_cells.append((y, x))
        return to_do_cells

    @staticmethod
    def solve_board(board, to_do_cells):
        done_cells = []
        while len(to_do_cells) > 0:
            current_cell = to_do_cells[0]
            result = SudokuSolver.solve_cell(board, current_cell)
            if result:
                board[current_cell[0]][current_cell[1]] = result
                done_cells.append(to_do_cells.pop(0))
            else:
                board[current_cell[0]][current_cell[1]] = 0
                to_do_cells.insert(0, done_cells.pop())
        return board
