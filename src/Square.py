from src.Figure import Figure


class Square(Figure):
    name = 'square'

    def __init__(self, side_a):
        if side_a <= 0:
            raise AttributeError
        self.side_a = side_a

    def get_area(self):
        if self.area == 0:
            self.area = self.side_a * self.side_a
        return self.area

    def get_perimeter(self):
        if self.perimeter == 0:
            self.perimeter = self.side_a * 4
        return self.perimeter





