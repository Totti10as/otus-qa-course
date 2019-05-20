from selenium.webdriver.common.by import By
from less7.base.selenium_webdriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    _username_Field = "input-username"
    _password_Field = "input-password"
    _login_button = "//button[@type='submit']"

# Methods to expose elements
    def getUsernameField(self):
        return self.driver.find_element(By.ID, self._username_Field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_Field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

# Methods to performs actions on the elements
    def enterUsername(self, username):
        self.getUsernameField().send_keys(username)

    def enterPassword(self, password):
        self.getUsernameField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

# API method to the methods above
    def login(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()
