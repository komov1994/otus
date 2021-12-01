from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

circle1 = Circle(12)
triangle1 = Triangle(12, 13, 14)
square1 = Square(12)
rectangle1 = Rectangle(12, 13)

figures = [circle1, triangle1, square1, rectangle1]
for item in figures:
    print(item.name, ': area = ', item.get_area(), ', perimeter = ', item.get_perimeter())

