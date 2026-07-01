import datetime
import pytest
import logging
from selenium import webdriver
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://localhost:8081/')
    parser.addoption('--log_level', default="INFO")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser')
    log_level = request.config.getoption('--log_level')
    base_url = request.config.getoption('url')

    logger = logging.getLogger(request.node.name)
    logs = Path('logs')
    logs.mkdir(exist_ok=True)
    screenshot = Path('screenshot')
    screenshot.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(f'logs/{request.node.name}.log', mode="w")
    file_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info('==> Test start at %s' % datetime.datetime.now())

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

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info('Browser %s started' % browser_name)
    yield driver

    def fin():
        driver.quit()
        logger.info('==> Test finished at %s' % datetime.datetime.now())
    request.addfinalizer(fin)
    return driver

