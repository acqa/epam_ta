import time
import pytest


testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())
testComment = 'Комментарий ' + str(time.gmtime())

@pytest.mark.run_these_please
def test_create_comment(app):
	# GIVEN заметку, если ее еще нет
	if app.article.count() == 0:
		app.article.create(articleTitle=testTitle, articleText=testNote)
	# WHEN создается комментарий
	app.comment.create(commentText = testComment)
	#  THEN комментарий создан
	# add assert
