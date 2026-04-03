from scr.rectangle import Rectangle


def test_area(input_side):
    r = Rectangle(input_side['side_a'], input_side['side_b'])
    assert r.area == 12, (f'Area of rectangle with side_a = {input_side['side_a']} '
                          f'and side_b = {input_side['side_b']} must be 12, actual is {r.area} ')


def test_perimetr(input_side):
    r = Rectangle(input_side['side_a'], input_side['side_b'])
    assert r.perimetr == 14, (f'Perimetr of rectangle with side_a = {input_side['side_a']} '
                              f'and side_b = {input_side['side_b']} must be 14, actual is {r.perimetr} ')
