import time

testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())
testComment = 'Комментарий ' + str(time.gmtime())


def test_create_comment(app):
	if app.article.count() == 0:
		app.article.create(articleTitle=testTitle, articleText=testNote)
	app.comment.create(commentText = testComment)
	# add assert
