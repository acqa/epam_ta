from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    def __init__(self, app):
        self.app = app

        wd = self.app.wd

        def open(self):
            wd.get(self.base_url + '/wp-login.php')

        # loginField = wd.find_element_by_id('user_login')
        # passField = wd.find_element_by_id('user_pass')
        # submitButton =  wd.find_element_by_id('wp-submit')


