import pytest
import pymysql.cursors


def pytest_addoption(parser):
    parser.addoption('--host', default='localhost')
    parser.addoption('--port', default='3307')
    parser.addoption('--database', default='prestashop')
    parser.addoption('--user', default='root')
    parser.addoption('--password', default='admin')


@pytest.fixture(scope="session")
def connection_db(request):
    host = request.config.getoption("--host")
    port = int(request.config.getoption("--port"))
    database = request.config.getoption("--database")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")

    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor,
    )
    yield conn
    conn.close()
