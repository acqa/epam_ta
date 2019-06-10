
class LoginPage():
    def __init__(self, app):
        self.app = app

    def login_field(self):
        wd = self.app.wd
        return wd.find_element_by_id('user_login')

    def password_field(self):
        wd = self.app.wd
        return wd.find_element_by_id('user_pass')

    def submit_button(self):
        wd = self.app.wd
        return wd.find_element_by_id('wp-submit')
