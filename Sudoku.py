class Sudoku:
    def get_row(self, position: tuple, board):
        return board[position[0]]

    def get_column(self, position: tuple, board):
        return [element[position[1]]
                for element in board]

    def get_horizontal_box_line(self, position, y, board):
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

    def get_box(self, position, board):
        box = list()
        if position[0] <= 2:
            for y in range(3):
                for element in self.get_horizontal_box_line(position, y, board):
                    box.append(element)
        elif position[0] <= 5:
            for y in range(3, 6):
                for element in self.get_horizontal_box_line(position, y, board):
                    box.append(element)
        elif position[0] <= 8:
            for y in range(6, 9):
                for element in self.get_horizontal_box_line(position, y, board):
                    box.append(element)
        else:
            return False
        return box

    def solve_cell(self, board, position):
        usedNumbers = set()
        usedNumbers = usedNumbers | set(self.get_row(position, board))
        usedNumbers = usedNumbers | set(self.get_column(position, board))
        usedNumbers = usedNumbers | set(self.get_box(position, board))
        i = board[position[0]][position[1]] + 1
        while True:
            if i not in usedNumbers and i <= 9:
                return i
            elif i > 9:
                return False
            else:
                i += 1
