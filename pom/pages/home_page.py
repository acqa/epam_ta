from pages.base_page import BasePage
import time


class HomePage(BasePage):

    def __init__(self, app):
        """Инициируем фикстуру арр и и получаем вебдрайвер из объекта фикстуры self.app.wd"""
        self.app = app

    def open(self):
        self.app.wd.get(self.app.base_url)


    #
    # def loginField(self):
    #     return self.app.wd.find_element_by_id('user_login')
    #
    # def passField(self):
    #     return self.app.wd.find_element_by_id('user_pass')
    #
    # def submit(self):
    #     return self.app.wd.find_element_by_id('wp-submit')
    #
    # def doLogin(self):
    #     self.loginField().send_keys("test_user")
    #     self.passField().send_keys("12345")
    #     self.submit().click()