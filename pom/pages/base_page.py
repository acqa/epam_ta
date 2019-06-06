from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, app):
        self.app = app



    # _URL = "http://duckduckgo.com"
    #
    # def __init__(self, driver: WebDriver) -> None:
    #     self._driver = driver

    def navigate_to(self, url):
        wd = self.app.wd
        wd.get(url)

    def get_element(self, locator: tuple, timeout=5):
        wd = self.app.wd
        return WebDriverWait(wd, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))

    def get_elements(self, locator: tuple, timeout=5):
        return WebDriverWait(wd, timeout).until(
            ex_cond.visibility_of_any_elements_located(locator), ' : '.join(locator))


# def open_home_page(self):
#     wd = self.wd
#     wd.get(self.base_url)