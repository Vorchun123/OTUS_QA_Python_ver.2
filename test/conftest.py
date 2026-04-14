import pytest


@pytest.fixture(scope='module')
def input_side():

    print("\nРасчитываем значение параметров area и perimetr для square")

    yield

    print('\nЗакончили расчет параметров area и perimetr для square')
