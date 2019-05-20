"""Conftest"""

import pytest
import sys
import logging
import less7.utillities.logger as cl
from less7.base.webdriverfactory import WebDriverFactory
from selenium import webdriver



def pytest_addoption(parser):
    """
    :param parser:
    parser adds the browser option to the command,
    so that we can use it with the command that we use to
    run test automation from terminal.
    :return:
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--address", action="store", default="http://192.168.1.26/", help="Opencart web address")


@pytest.fixture(scope="session")
def browser(request):
    """
    Fixture to select relevant browser
    """
    return request.config.getoption("--browser")


@pytest.fixture()
def setUP():
    log = cl.customLogger(logging.DEBUG)
    log.info("Running method level setUp")
    yield
    log.info("Running method level tearDown")



@pytest.fixture(scope="class")
def driver(request, browser):
    log = cl.customLogger(logging.DEBUG)
    log.info("Running browser setup selection")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    """  
    Provides driver at the class level to all the classes
    that are using conftest, so that driver is available for them to use.
    """
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.close()
    driver.quit()
    log.info("\nClose browser window and quit the Driver")
    log.info(sys.path)
