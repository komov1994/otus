import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


# SQUARE
@pytest.fixture
def default_square():
    square = Square(4)
    yield square
    del square


@pytest.fixture
def incorrect_square_minus():
    return -12


@pytest.fixture
def incorrect_square_zero():
    return 0


# CIRCLE
@pytest.fixture
def default_circle():
    circle = Circle(2)
    yield circle
    del circle


@pytest.fixture
def incorrect_circle_minus():
    circle = -12
    yield circle
    del circle


@pytest.fixture
def incorrect_circle_zero():
    circle = 0
    yield circle
    del circle


# RECTANGLE
@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(12, 13)
    yield rectangle
    del rectangle


@pytest.fixture
def incorrect_rectangle_minus():
    rectangle = [-12, 3]
    yield rectangle
    del rectangle


@pytest.fixture
def incorrect_rectangle_zero():
    rectangle = [5, 0]
    yield rectangle
    del rectangle


# TRIANGLE
@pytest.fixture
def default_triangle():
    triangle = Triangle(12, 13, 14)
    yield triangle
    del triangle


@pytest.fixture
def incorrect_triangle_minus():
    triangle = [7, -3, 6]
    yield triangle
    del triangle


@pytest.fixture
def incorrect_triangle_zero():
    triangle = [5, 4, 0]
    yield triangle
    del triangle
