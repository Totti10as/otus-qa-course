"""Conftest"""

import pytest
import sys
from selenium import webdriver



# Import and declare on plugins from the fixtures files
pytest_plugins = ['login_fixtures']



def pytest_addoption(parser):
    """
    :param parser:
    parser adds the browser option to the command,
    so that we can use it with the command that we use to
    run test automation from terminal.
    :return:
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--address", action="store", default="http://192.168.1.26/opencart/admin/", help="Opencart web address")


@pytest.fixture(scope="session")
def browser(request):
    """
    :param request:
    Read the parameters from the command line
    and add to the request config which the code can use.
    :return:
    """
    return request.config.getoption("--browser")


@pytest.fixture(scope="module", autouse=True)
def driver(browser):
    """ Fixture to select relevant browser"""
    print("Running browser setup selection")
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(2)
        print("Running tests in Chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(2)
        print("Running tests in FF")
    else:
        print('Unsupported browser!')
        sys.exit(1)

    yield driver
    driver.close()
    driver.quit()
    print("\nClose browser window and quit the Driver")
    print(sys.path)

