import pytest

from scr.square import Square


@pytest.mark.parametrize('side_a', [3, 56, 2.5])
def test_area(side_a):
    s = Square(side_a)
    assert s.area == 9


@pytest.mark.parametrize('side_a', [3, 56, 2.5])
def test_perimetr(side_a):
    s = Square(side_a)
    assert s.perimetr == 12
