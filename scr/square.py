from scr.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a: float):
        if side_a <= 0:
            raise ValueError(f"side_a must be above zero now side_a = {side_a}")
        super().__init__(side_a, side_a)

        self.side_a = side_a

    @property
    def area(self):
        return self.side_a**2

    @property
    def perimetr(self):
        return (self.side_a + self.side_a) * 2
