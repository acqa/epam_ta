from pages.base_page import BasePage
import time


class ArticlePage(BasePage):

    def __init__(self, app):
        """Инициируем фикстуру арр и и получаем вебдрайвер из объекта фикстуры self.app.wd"""
        self.app = app

    """Элементы страницы"""

    def titleText(self):
        try:
            return self.app.wd.find_element_by_xpath('//h1[@class = "entry-title"]').text
        except:
            return None

    def noteText(self):
        try:
            return self.app.wd.find_element_by_xpath('//div[@class = "entry-content"]/p').text
        except:
            return None



