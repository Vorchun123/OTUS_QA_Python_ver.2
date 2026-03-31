from scr.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(
                f"side_a and side_b must be above zero now side_a = {side_a}, side_b = {side_b}"
            )
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimetr(self):
        return (self.side_a + self.side_b) * 2
