from scr.figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError(
                f"radius must be above zero now radius = {radius}"
            )
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimetr(self):
        return 2 * math.pi + self.radius
