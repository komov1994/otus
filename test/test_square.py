import pytest
from src.Square import Square


@pytest.mark.parametrize("side_a, area", [(5, 25), (9, 81), (15, 225)])
def test_area_square(side_a, area):
    square = Square(side_a).get_area()
    assert square == area


@pytest.mark.parametrize("side_a, perimeter", [(5, 20), (9, 36), (15, 60)])
def test_perimeter_square(side_a, perimeter):
    square = Square(side_a).get_perimeter()
    assert square == perimeter


def test_negative_square_minus(incorrect_square_minus):
    with pytest.raises(AttributeError):
        Square(incorrect_square_minus)


def test_negative_square_zero(incorrect_square_zero):
    with pytest.raises(AttributeError):
        Square(incorrect_square_zero)


def test_add_area_circle(default_square, default_circle):
    assert default_square.add_area(default_circle) == 28.566370614359172


def test_add_area_rectangle(default_square, default_rectangle):
    assert default_square.add_area(default_rectangle) == 172


def test_add_area_triangle(default_square, default_triangle):
    assert default_square.add_area(default_triangle) == 88.30793524918272

