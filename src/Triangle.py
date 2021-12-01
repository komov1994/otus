import math
from src.Figure import Figure


class Triangle(Figure):
    name = 'triangle'

    def __init__(self, side_a, side_b, side_c):
        if (((side_a <= 0) or (side_b <= 0) or (side_c <= 0)) and
                ((self.side_a < self.side_b + self.side_c) and
                (self.side_b < self.side_a + self.side_c) and
                (self.side_c < self.side_a + self.side_b))):
            raise AttributeError
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        if self.area == 0:
            p = (self.side_a + self.side_b + self.side_c) / 2
            self.area = math.sqrt((p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)))
        return self.area

    def get_perimeter(self):
        if self.perimeter == 0:
            self.perimeter = self.side_a + self.side_b + self.side_c
        return self.perimeter

