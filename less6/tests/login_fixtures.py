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


@pytest.fixture(scope="function")
def login_valid(driver, open_login_page):
    """
    Tests steps for valid login
    """
    login = LoginPage(driver)
    login.enter_username("admin")
    login.enter_password("admin")
    login.click_login()
    time.sleep(2)  # Testing it - Remove after test



@pytest.fixture(scope="function")
def login_invalid(driver, open_login_page):
    """
        Tests steps for invalid login
    """
    login = LoginPage(driver)
    login.enter_username("admin")
    login.enter_password("admin1")
    login.click_login()
    message = login.check_invalid_error_message()
    time.sleep(2)  # Testing it - Remove after test
    return message
