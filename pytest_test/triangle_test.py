from scr.triangle import Triangle
import pytest


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [pytest.param(12, 13, 0, id='zero'),
                          pytest.param(-3, 5, 9, id='negative number'),
                          pytest.param(12, 4, 5, id='non-existent triangle')
                          ])
def test_area_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
