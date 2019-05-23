import time


# Test data
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())
testdata = {"testTitle":testTitle, "testNote":testNote}





#@pytest.mark.parametrize("article", testdata)
def test_create_article(app):
	app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])


def test_check_article(app):
	app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	app.article.check(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
