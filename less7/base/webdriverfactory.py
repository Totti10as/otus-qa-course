"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

import logging
import pytest
import sys
import less7.utillities.logger as cl
from selenium import webdriver


class WebDriverFactory():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """

        self.browser = browser
        """
               Set chrome driver and iexplorer environment based on OS

               chromedriver = "C:/.../chromedriver.exe"
               os.environ["webdriver.chrome.driver"] = chromedriver
               self.driver = webdriver.Chrome(chromedriver)

               PREFERRED: Set the path on the machine where browser will be executed
        """

    def getWebDriverInstance(self):

        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        # baseURL = 'http://192.168.1.26/opencart/admin/'
        self.log.info("Running browser setup selection")
        if self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
            self. log.info("Running tests in Chrome")
        elif self.browser == "firefox":
            # Set chrome driver
            driver = webdriver.Firefox()
            self.log.info("Running tests in Firefox")
        else:
            self.log.info('Unsupported browser!')
            sys.exit(1)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Set the window size
        driver.set_window_size(1200, 800)
        # Loading browser with App URL
        #driver.get(baseURL)
        return driver



