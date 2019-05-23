import time
from model.article import Article


# Test data
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())
testdata = {"testTitle":testTitle, "testNote":testNote}







#@pytest.mark.parametrize("article", testdata)
def test_create_article(app):
	#app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))


def test_check_article(app):
	app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
	#app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	app.article.check(Article(title=testdata['testTitle'], note=testdata['testNote']))
