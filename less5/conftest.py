"""Conftest"""

import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    """
    :return: Setup
    """
    print('Running method level setUp')
    yield
    print('Running method level tearDown')


@pytest.fixture(scope="module")
def selectbrowser(browser):
    """ Fixture to select relevant browser"""
    print("Running browser setup selection")
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--proxy-server='direct://'")  # Improving headless slowness issue on Win 7
        options.add_argument("--proxy-bypass-list=*")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(3)
        print("Running tests Chrome-headless")
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--proxy-server='direct://'")  # Improving headless slowness issue on Win 7
        options.add_argument("--proxy-bypass-list=*")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(1)
        print("Running tests FF-headless")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)

    yield driver
    driver.close()
    driver.quit()
    print("\nClose browser window and quit the Driver")


def pytest_addoption(parser):
    """
    :param parser:
    parser adds the browser option to the command,
    so that we can use it with the command that we use to
    run test automation from terminal.

    :return:
    """
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    """
    :param request:
    Read the parameters from the command line
    and add to the request config which the code can use.
    :return:
    """
    return request.config.getoption("--browser")
