import pytest

from scr.rectangle import Rectangle


@pytest.mark.parametrize(('side_a', 'side_b', 'area'),
                         [pytest.param(4, 6, 24, id='integer'),
                          pytest.param(5.5, 6.5, 33, id='float')])
def test_get_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, (f'Area of rectangle with side_a = {side_a} '
                            f'and side_b = {side_b} must be 12, actual is {r.area} ')
