from less6.locators.locators import Locators


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath
        self.invalid_username_message_xpath = Locators.invalid_username_message_xpath

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def check_invalid_error_message(self):
        msg = self.driver.find_element_by_xpath(self.invalid_username_message_xpath).text
        return msg





