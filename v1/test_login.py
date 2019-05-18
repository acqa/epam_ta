from application import Application
import pytest

# def is_alert_present(wd):
# 	try:
# 		wd.switch_to_alert().text
# 		return True
# 	except:
# 		return False


@pytest.fixture
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture

def test_login(app):
	app.login(username = 'test_user', password = '12345')
	#app.logout()

def test_create_article(app):
	app.login(username = 'test_user', password = '12345')
	app.create_article(articleTitle='Title', articleText='Text')
	#app.logout()

def test_check_article(app):
	app.login(username = 'test_user', password = '12345')
	app.create_article(articleTitle='Title', articleText='Text')
	app.check_article(articleTitle='Title', articleText='Text')
	#app.logout()






		