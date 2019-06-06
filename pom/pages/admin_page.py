from pages.base_page import BasePage

class AdminPage(BasePage):

    def __init__(self, app):
        """Инициируем фикстуру арр и и получаем вебдрайвер из объекта фикстуры self.app.wd"""
        self.app = app

    def open(self):
        self.app.wd.get(self.app.base_url + '/wp-admin/')
