class SudokuBoard:
    def __init__(self, boardArray=0):
        self.board = boardArray

    def get_row(self, position: tuple):
        return self.board[position[1]]

    def get_column(self, position: tuple):
        return [element[position[0]]
                for element in self.board]

    def get_horizontal_box_line(self, position, x):
        box = list()
        if position[1] <= 2:
            for y in range(3):
                box.append(self.board[y][x])
        elif position[1] <= 5:
            for y in range(3, 6):
                box.append(self.board[y][x])
        elif position[1] <= 8:
            for y in range(6, 9):
                box.append(self.board[y][x])
        else:
            return False
        return box

    def get_box(self, position):
        box = list()
        if position[0] <= 2:
            for x in range(3):
                for element in self.get_horizontal_box_line(position, x):
                    box.append(element)
        elif position[0] <= 5:
            for x in range(3, 6):
                for element in self.get_horizontal_box_line(position, x):
                    box.append(element)
        elif position[0] <= 8:
            for x in range(6, 9):
                for element in self.get_horizontal_box_line(position, x):
                    box.append(element)
        else:
            return False
        return box
