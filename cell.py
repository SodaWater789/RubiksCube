class Cell:
    def __init__(self, color = None, point = None, norm = None):
        self.color = color
        self.point = point
        self.norm = norm

    def __str__(self):
        return self.color