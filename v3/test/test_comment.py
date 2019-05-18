import time

testLogin = 'test_user'
testPassword = '12345'
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())
testComment = 'Комментарий ' + str(time.gmtime())


def test_create_comment(app):
	app.session.login(username = testLogin, password = testPassword)
	app.article.create(articleTitle=testTitle, articleText=testNote)
	app.article.check(articleTitle=testTitle, articleText=testNote)
	app.comment.create(commentText = testComment)