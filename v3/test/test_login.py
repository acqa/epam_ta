import time

testLogin = 'test_user'
testPassword = '12345'
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())


def test_login(app):
	app.session.login(username = testLogin, password = testPassword)
	#app.session.logout()






		