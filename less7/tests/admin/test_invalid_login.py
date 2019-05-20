from selenium import webdriver
from less7.pages.admin.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_invalid_login(self):
        baseurl = "http://192.168.1.26/opencart/admin/"
        driver = webdriver.Chrome()
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(2)
        driver.get(baseurl)

        lp = LoginPage(driver)
        lp.login("admin", "")
        result = lp.verifyiLoginFailed()

        assert result

        driver.close()
        driver.quit()
