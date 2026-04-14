from scr.square import Square


def test_area(input_side, side_a=12):
    s = Square(side_a)
    assert s.area == 9, f'Area of square with side_a = {side_a} must be 9, actual is {s.area}'


def test_perimetr(input_side, side_a=12):
    s = Square(side_a)
    assert s.perimetr == 12, f'Perimetr of square with side_a = {side_a} must be 12, actual is {s.perimetr}'
