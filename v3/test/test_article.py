import time

testLogin = 'test_user'
testPassword = '12345'
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())

def test_create_article(app):
	app.session.login(username = testLogin, password = testPassword)
	app.article.create(articleTitle=testTitle, articleText=testNote)
	#app.logout()

def test_check_article(app):
	app.session.login(username = testLogin, password = testPassword)
	app.article.create(articleTitle=testTitle, articleText=testNote)
	app.article.check(articleTitle=testTitle, articleText=testNote)