from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    def __init__(self, app):
        """Инициируем фикстуру арр и и получаем вебдрайвер из объекта фикстуры self.app.wd"""
        self.app = app

    def open(self):
        self.app.wd.get(self.app.base_url + '/wp-login.php')

    def loginField(self):
        return self.app.wd.find_element_by_id('user_login')

    def passField(self):
        return self.app.wd.find_element_by_id('user_pass')

    def submitButton(self):
        return self.app.wd.find_element_by_id('wp-submit')

    def fix_login(self, login, password):
        """Фикстура для авторизации в админ-панели, до запуска тестов"""
        self.open()
        self.loginField().send_keys(login)
        self.passField().send_keys(password)
        self.submitButton().click()



