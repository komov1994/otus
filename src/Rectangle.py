from src.Figure import Figure


class Rectangle(Figure):
    name = 'rectangle'

    def __init__(self, side_a, side_b):
        if (side_a <= 0) or (side_b <= 0):
            raise AttributeError
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        if self.area == 0:
            self.area = self.side_a * self.side_b
        return self.area

    def get_perimeter(self):
        if self.perimeter == 0:
            self.perimeter = 2 * (self.side_a + self.side_b)
        return self.perimeter


