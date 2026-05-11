import requests


def test_get_addoption(url, status_code):
    response = requests.get(url)
    assert str(response.status_code) == status_code
