from pages.base_page import BasePage
import time


class PostPage(BasePage):

    def __init__(self, app):
        """Инициируем фикстуру арр и и получаем вебдрайвер из объекта фикстуры self.app.wd"""
        self.app = app

    def open(self):
        self.app.wd.get(self.app.base_url + '/wp-admin/post-new.php')

    def fix_close_advice_popup(self):
        """Фикстура для закрытия pop-up окна при первом открытии страницы"""
        self.open()
        self.closeAdviceButton().click()



    """Элементы страницы"""

    def titleField(self):
        return self.app.wd.find_element_by_id('post-title-0')

    def noteField(self):
        self.app.wd.find_element_by_xpath('//textarea[@class = "editor-default-block-appender__content block-editor-default-block-appender__content"]').click()
        return self.app.wd.find_element_by_xpath('//p[@class = "block-editor-rich-text__editable editor-rich-text__editable wp-block-paragraph"]')

    def publishButton(self):
        return self.app.wd.find_element_by_xpath('//button[@class = "components-button editor-post-publish-panel__toggle is-button is-primary"]')

    def publishConfirmButton(self):
        return self.app.wd.find_element_by_xpath('//button[@class = "components-button editor-post-publish-button is-button is-default is-primary is-large"]')

    def closeAdviceButton(self):
        return self.app.wd.find_element_by_xpath('//button[@class = "components-button components-icon-button nux-dot-tip__disable"]')

    def articleUrlInput(self):
        return self.app.wd.find_element_by_xpath('//input[@class = "components-text-control__input"]').get_attribute('defaultValue')



    """Выполнение действий для тестов"""

    def create_article(self, title, note):
        self.open()
        self.titleField().send_keys(title)
        self.noteField().send_keys(note)
        self.publishButton().click()
        self.publishConfirmButton().click()
        self.app.wd.get(self.articleUrlInput())









