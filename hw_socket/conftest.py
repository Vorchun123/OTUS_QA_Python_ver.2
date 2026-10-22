import pytest


@pytest.fixture(scope="session")
def host():
    return "127.0.0.1"


@pytest.fixture(scope="session")
def port():
    return 8080
