from fixture.application import Application
import data.data
import pytest
import time

# def is_alert_present(wd):
# 	try:
# 		wd.switch_to_alert().text
# 		return True
# 	except:
# 		return False

testLogin = 'test_user'
testPassword = '12345'
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())


@pytest.fixture
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture

def test_login(app):
	app.session.login(username = testLogin, password = testPassword)
	#app.session.logout()

def test_create_article(app):
	app.session.login(username = testLogin, password = testPassword)
	app.article.create(articleTitle=testTitle, articleText=testNote)
	#app.logout()

def test_check_article(app):
	app.session.login(username = testLogin, password = testPassword)
	app.article.create(articleTitle=testTitle, articleText=testNote)
	app.article.check(articleTitle=testTitle, articleText=testNote)
	#app.session.logout()






		