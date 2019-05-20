
from less7.base.basepage import BasePage
import less7.utillities.logger as cl
import logging
import time


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    _username_Field_Id = "input-username"
    _password_Field_Id = "input-password"
    _login_button_Xpath = "//button[@type='submit']"
    _popup_dismiss_Class = "close"

# Methods to performs actions on the elements
    def enterUsername(self, username):
        self.sendKeys(username, self._username_Field_Id)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Field_Id)

    def clickLoginButton(self):
        self.elementClick(self._login_button_Xpath, locatorType="Xpath")

    def clickPopupClose(self):
        self.elementClick(self._popup_dismiss_Class, locatorType="classname")

# API method to the methods above (Wrapper functionality)
    def login(self, username="", password=""):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()
        self.clickPopupClose()



    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@class='modal-header']//h4[contains(text(),"
                                       "' Important Security Notification!')]", locatorType="xpath")
        return result

    def verifyiLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'No match for Username and/or Password')]"
                                       , locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Dashboard")




