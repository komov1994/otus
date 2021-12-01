import pytest
from src.Circle import Circle


@pytest.mark.parametrize("radius, area", [(5, 78.53981633974483), (9, 254.46900494077323), (15, 706.8583470577034)])
def test_area_circle(radius, area):
    circle = Circle(radius).get_area()
    assert circle == area


@pytest.mark.parametrize("radius, perimeter",
                         [(5, 31.41592653589793), (9, 56.548667764616276), (15, 94.24777960769379)])
def test_perimeter_square(radius, perimeter):
    circle = Circle(radius).get_perimeter()
    assert circle == perimeter


def test_negative_circle_minus(incorrect_circle_minus):
    with pytest.raises(AttributeError):
        Circle(incorrect_circle_minus)


def test_negative_square_zero(incorrect_circle_zero):
    with pytest.raises(AttributeError):
        Circle(incorrect_circle_zero)


def test_add_area_rectangle(default_circle, default_rectangle):
    assert default_circle.add_area(default_rectangle) == 168.5663706143592


def test_add_area_triangle(default_circle, default_triangle):
    assert default_circle.add_area(default_triangle) == 84.87430586354189

