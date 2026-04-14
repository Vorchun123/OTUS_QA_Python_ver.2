from scr.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(
                f"side_a, side_b, side_c must be above zero now side_a = {side_a}, side_b = {side_b}, side_c = {side_c}"
            )
        if side_a >= (side_b + side_c) or side_b >= (side_c + side_a) or side_c >= (side_b + side_a):
            raise ValueError('triangle cannot exist because one of the sides is greater than the sum of the other two')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        half_perimetr = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt((half_perimetr * (half_perimetr - self.side_a) * (half_perimetr - self.side_b) *
                          (half_perimetr - self.side_c)))

    @property
    def perimetr(self):
        return self.side_a + self.side_b + self.side_c
