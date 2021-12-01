from src.Figure import Figure
import math


class Circle(Figure):
    name = 'circle'

    def __init__(self, radius):
        if radius <= 0:
            raise AttributeError
        self.radius = radius

    def get_area(self):
        if self.area == 0:
            self.area = self.radius * self.radius * math.pi
        return self.area

    def get_perimeter(self):
        if self.perimeter == 0:
            self.perimeter = self.radius * 2 * math.pi
        return self.perimeter


