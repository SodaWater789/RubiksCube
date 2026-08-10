from cell import Cell

class Cube:
    def __init__(self):
        self.cells = []
        self.dim = (3, 3)
        self.build_cube()

    def build_cube(self):

        self.build_front()
        self.build_back()
        self.build_left()
        self.build_right()
        self.build_top()
        self.build_bottom()
    def build_front(self):

        # z = 1
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cell = Cell(color = "G", point=(i, j, 1), norm=(0, 0, 1))
                self.cells.append(cell)

    def build_back(self):

        # z = -1
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cell = Cell(color = "B", point=(i, j, -1), norm=(0, 0, -1))
                self.cells.append(cell)

    def build_left(self):

        # x = -1
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cell = Cell(color = "R", point=(-1, i, j), norm=(-1, 0, 0))
                self.cells.append(cell)

    def build_right(self):

        # x = 1
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cell = Cell(color = "O", point=(1, i, j), norm=(1, 0, 0))
                self.cells.append(cell)

    def build_top(self):

        # y = 1
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cell = Cell(color = "Y", point=(i, 1, j), norm=(0, 1, 0))
                self.cells.append(cell)

    def build_bottom(self):

        # y = -1
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cell = Cell(color = "W", point=(i, -1, j), norm=(0, -1, 0))
                self.cells.append(cell)

if __name__ == "__main__":
    cube = Cube()
    for cell in cube.cells:
        print(cell.point, cell.norm, cell.color)