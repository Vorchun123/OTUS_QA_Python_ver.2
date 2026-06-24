import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://localhost:8081/')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser')
    base_url = request.config.getoption('url')

    driver = None

    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'edge':
        driver = webdriver.Edge()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f'Browser {browser_name} is not supported')
    driver.get(base_url)
    driver.set_window_size(1920, 1080)
    yield driver

    driver.quit()
