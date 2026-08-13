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

    def move_R(self):
        for cell in self.cells:
            x, y, z = cell.point
            if x == 1:
                cell.point = (x, z, -y)
                nx, ny, nz = cell.norm
                cell.norm = (nx, nz, -ny)

    def move_R_prime(self):
        for cell in self.cells:
            x, y, z = cell.point
            if x == 1:
                cell.point = (x, -z, y)
                nx, ny, nz = cell.norm
                cell.norm = (nx, -nz, ny)

    def move_L(self):
        for cell in self.cells:
            x, y, z = cell.point
            if x == -1:
                cell.point = (x, -z, y)
                nx, ny, nz = cell.norm
                cell.norm = (nx, -nz, ny)

    def move_L_prime(self):
        for cell in self.cells:
            x, y, z = cell.point
            if x == -1:
                cell.point = (x, z, -y)
                nx, ny, nz = cell.norm
                cell.norm = (nx, nz, -ny)

    def move_U(self):
        for cell in self.cells:
            x, y, z = cell.point
            if y == 1:
                cell.point = (-z, y, x)
                nx, ny, nz = cell.norm
                cell.norm = (-nz, ny, nx)

    def move_U_prime(self):
        for cell in self.cells:
            x, y, z = cell.point
            if y == 1:
                cell.point = (z, y, -x)
                nx, ny, nz = cell.norm
                cell.norm = (nz, ny, -nx)

    def move_D(self):
        for cell in self.cells:
            x, y, z = cell.point
            if y == -1:
                cell.point = (z, y, -x)
                nx, ny, nz = cell.norm
                cell.norm = (nz, ny, -nx)

    def move_D_prime(self):
        for cell in self.cells:
            x, y, z = cell.point
            if y == -1:
                cell.point = (-z, y, x)
                nx, ny, nz = cell.norm
                cell.norm = (-nz, ny, nx)

    def move_F(self):
        for cell in self.cells:
            x, y, z = cell.point
            if z == 1:
                cell.point = (y, -x, z)
                nx, ny, nz = cell.norm
                cell.norm = (ny, -nx, nz)

    def move_F_prime(self):
        for cell in self.cells:
            x, y, z = cell.point
            if z == 1:
                cell.point = (-y, x, z)
                nx, ny, nz = cell.norm
                cell.norm = (-ny, nx, nz)

    def move_B(self):
        for cell in self.cells:
            x, y, z = cell.point
            if z == -1:
                cell.point = (-y, x, z)
                nx, ny, nz = cell.norm
                cell.norm = (-ny, nx, nz)

    def move_B_prime(self):
        for cell in self.cells:
            x, y, z = cell.point
            if z == -1:
                cell.point = (y, -x, z)
                nx, ny, nz = cell.norm
                cell.norm = (ny, -nx, nz)

    def sequence(self, move_string):

        move_map = {
            "R": self.move_R,
            "R'": self.move_R_prime,
            "L": self.move_L,
            "L'": self.move_L_prime,
            "U": self.move_U,
            "U'": self.move_U_prime,
            "D": self.move_D,
            "D'": self.move_D_prime,
            "F": self.move_F,
            "F'": self.move_F_prime,
            "B": self.move_B,
            "B'": self.move_B_prime
        }

        if isinstance(move_string, str):
            move_string = move_string.split()

        for move in move_string:
            if move in move_map:
                move_map[move]()

    def scramble(self):
        import random
        moves = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]

        num_moves = random.randint(10, 30)
        scramble_moves = random.choices(moves, k = num_moves)
        self.sequence(scramble_moves)

if __name__ == "__main__":
    cube = Cube()
    for cell in cube.cells:
        print(cell.point, cell.norm, cell.color)
    cube.move_R()
    for cell in cube.cells:
        print("After move R:", cell.point, cell.norm, cell.color)