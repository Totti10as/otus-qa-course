from selenium import webdriver
from less7.pages.admin.login_page import LoginPage
import unittest
import pytest

@pytest.fixture(scope="class")
def open_login_page(driver, request):
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("open_login_page")
class TestLogin(object):


    @pytest.fixture(autouse=True)
    def classSetup(self, driver):
        self.lp = LoginPage(self.driver)

    def test_valid_login(self):
        self.lp.login("admin", "admin")
        result1 = self.lp.verifyLoginSuccessful()
        assert result1
        result2 = self.lp.verifyLoginTitle()
        assert result2







