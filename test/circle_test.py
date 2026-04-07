from scr.circle import Circle
import pytest
radius = 3


@pytest.mark.skip(reason="for example")
def test_area():
    c = Circle(radius)
    assert c.area == 15.4, f'Area of circle with radius  = {radius}  must be 15.4, actual is {c.area} '


@pytest.mark.skipif(condition=radius <= 5, reason="very small")
def test_perimetr():
    c = Circle(radius)
    assert c.perimetr == 15.4
