from app.application import App
import pytest


#testdata
base_url = "http://v999140x.beget.tech"
login ="test_user"
password ="12345"

@pytest.fixture(scope = 'session')
def app(request):
	app = App(base_url = base_url)
	app.login_page.fix_login(login = login, password = password)
	app.post_page.fix_close_advice_popup()
	yield app
	app.destroy()
