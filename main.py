class Game:
    def __init__(self, row, col) -> None:
        self.board = Board(row, col)

    def change_state(self, row, col, state):
        for r in range(self.board.get_row()):
            for c in range(self.board.get_column()):
                pass
            print()

class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cells = [[0]*row for i in range(col)]

    def set_state(self, row, col, state):
        self.cells[col][row] = state

    def get_state(self, row, col):
        return self.cells[row][col]

    def print_board(self):
        for r in range(self.row):
            for c in range(self.col):
                print(self.cells[c][r], end=" ")
            print()

    def __str__(self) -> str:
        return str(self.cells)

    def get_row(self):
        return self.row

    def get_column(self):
        return self.col

if __name__ == "__main__":
    game = Game(10, 20)
    game.change_state(5,5,1)
    game.board.print_board()
