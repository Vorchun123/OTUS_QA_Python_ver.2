import pytest


@pytest.fixture(scope='function')
def input_side():

    a = int(input("\nВведите значение первой стороны - side_a:"))
    b = int(input("Введите значение второй стороны - side_b:"))
    return {'side_a': a, "side_b": b}
