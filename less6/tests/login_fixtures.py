""" Use fixtures on testing login page """

import time
import pytest
from less6.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def open_login_page(driver, request):
    """
    get relevant driver
    return open default url
    """
    return driver.get("".join([request.config.getoption("--address")]))

@pytest.fixture(scope="module")
def login_page(driver):
    """ Create and allow using of object attributes"""
    return LoginPage(driver)



@pytest.fixture(scope="function")
def login_valid(login_page, open_login_page):
    """
    Tests steps for valid login
    """
    login_page.enter_username("admin")
    login_page.enter_password("admin")
    login_page.click_login()
    time.sleep(2)  # Testing it - Remove after test


@pytest.fixture(scope="function")
def login_invalid(login_page, open_login_page):
    """
        Tests steps for invalid login
    """
    login_page.enter_username("admin")
    login_page.enter_password("admin1")
    login_page.click_login()
    message = login_page.check_invalid_error_message()
    time.sleep(2)  # Testing it - Remove after test
    return message
