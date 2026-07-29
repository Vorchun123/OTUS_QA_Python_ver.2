import datetime
import pytest
import logging
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://192.168.10.247:8081/')
    parser.addoption('--headless', action='store_true', default=False)
    parser.addoption('--log_level', default="INFO")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser')
    log_level = request.config.getoption('log_level')
    headless = request.config.getoption('headless')
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

    chrom_options = ChromeOptions()
    edge_options = EdgeOptions()
    firefox_options = FirefoxOptions()

    if browser_name == 'chrome':
        chrom_options.add_argument('--no-sandbox')
        chrom_options.add_argument('--disable-dev-shm-usage')
        if headless:
            chrom_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrom_options)
    elif browser_name == 'edge':
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--disable-dev-shm-usage')
        if headless:
            edge_options.add_argument('headless')
        driver = webdriver.Edge(options=edge_options)
    elif browser_name == 'firefox':
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--disable-dev-shm-usage')
        if headless:
            firefox_options.add_argument('headless')
        driver = webdriver.Firefox(options=firefox_options)
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

