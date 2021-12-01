import pytest
from src.Triangle import Triangle


@pytest.mark.parametrize("side_a, side_b, side_c, area", [(2, 4, 5, 3.799671038392666),
                                                          (3, 5, 7, 6.49519052838329),
                                                          (7, 4, 9, 13.416407864998739)])
def test_area_triangle(side_a, side_b, side_c, area):
    triangle = Triangle(side_a, side_b, side_c).get_area()
    assert triangle == area


@pytest.mark.parametrize("side_a, side_b, side_c, perimeter", [(2, 4, 5, 11),
                                                               (3, 5, 7, 15),
                                                               (7, 4, 9, 20)])
def test_perimeter_triangle(side_a, side_b, side_c, perimeter):
    triangle = Triangle(side_a, side_b, side_c).get_perimeter()
    assert triangle == perimeter


def test_negative_triangle_minus(incorrect_triangle_minus):
    with pytest.raises(AttributeError):
        Triangle(incorrect_triangle_minus[0],
                 incorrect_triangle_minus[1],
                 incorrect_triangle_minus[2])


def test_negative_triangle_zero(incorrect_triangle_zero):
    with pytest.raises(AttributeError):
        Triangle(incorrect_triangle_zero[0],
                 incorrect_triangle_zero[1],
                 incorrect_triangle_zero[2])
