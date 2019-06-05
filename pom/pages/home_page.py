from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, app):
        self.app = app

        def open(self):
            wd = self.app.wd
            wd.get(self.base_url)


        # def open(self):
        #     super().navigate_to(app.base_url)
        #     return self
        #

    #
    #
    # def open(self):
    #     super().navigate_to(super()._URL)
    #
    #
    #
    #
    #
    #
    # class SearchPage(BasePage):
    #
    #     def __init__(self, app):
    #         self.app = app
    #
    #         self.base_url
    #
    #     _search_field = (By.ID, "search_form_input_homepage")
    #
    #     def open(self):
    #         super().navigate_to(app.base_url)
    #         return self
    #
    #     @allure.step("search for {text}")
    #     def search_for(self, text):
    #         super().get_element(self._search_field).send_keys(text)
    #         super().get_element(self._search_field).submit()
    #         return ResultPage(self._driver)


# def open_home_page(self):
#     wd = self.wd
#     wd.get(self.base_url)