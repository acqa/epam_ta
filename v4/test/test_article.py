import time

testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())

def test_create_article(app):
	app.article.create(articleTitle=testTitle, articleText=testNote)


def test_check_article(app):
	app.article.create(articleTitle=testTitle, articleText=testNote)
	app.article.check(articleTitle=testTitle, articleText=testNote)
