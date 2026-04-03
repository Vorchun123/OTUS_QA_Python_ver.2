from scr.circle import Circle
import pytest


@pytest.mark.skip(reason="for example")
def test_area():
    c = Circle(6.5)
    assert c.area == 15.4


radius = 6


@pytest.mark.skipif(condition=radius <= 5, reason="very small")
def test_perimetr():
    c = Circle(radius)
    assert c.perimetr == 15.4
