""" Locators page """


class Locators(object):

    # Login page objects
    username_textbox_id = "input-username"
    password_textbox_id = "input-password"
    login_button_xpath = "//button[@type='submit']"
    invalid_username_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"
