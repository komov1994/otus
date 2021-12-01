import pytest
from src.Rectangle import Rectangle


@pytest.mark.parametrize("side_a, side_b, area", [(2, 4, 8), (3, 5, 15), (7, 4, 28)])
def test_area_rectangle(side_a, side_b, area):
    rectangle = Rectangle(side_a, side_b).get_area()
    assert rectangle == area


@pytest.mark.parametrize("side_a, side_b, perimeter", [(2, 4, 12), (3, 5, 16), (7, 4, 22)])
def test_perimeter_rectangle(side_a, side_b, perimeter):
    rectangle = Rectangle(side_a, side_b).get_perimeter()
    assert rectangle == perimeter


def test_negative_rectangle_minus(incorrect_rectangle_minus):
    with pytest.raises(AttributeError):
        Rectangle(incorrect_rectangle_minus[0],
                  incorrect_rectangle_minus[1])


def test_negative_rectangle_zero(incorrect_rectangle_zero):
    with pytest.raises(AttributeError):
        Rectangle(incorrect_rectangle_zero[0],
                  incorrect_rectangle_zero[1])


def test_add_area_triangle(default_rectangle, default_triangle):
    assert default_rectangle.add_area(default_triangle) == 228.30793524918272

