from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, app):
        self.app = app  #

    def waitVisibility(self):
