from model.article import Article
import pytest
from data.add_article import testdata_static
from data.add_article import testdata_random



@pytest.mark.parametrize("article", testdata_random, ids = [repr(x) for x in testdata_random])
def test_create_article_param(app, article):
	pass
	##app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	#app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
	app.article.create(article)


@pytest.mark.parametrize("article", testdata_static, ids = [repr(x) for x in testdata_static])
def test_create_article(app, article):
	#app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	#app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
	app.article.create(article)


@pytest.mark.parametrize("article", testdata_static, ids = [repr(x) for x in testdata_static])
def test_check_article(app, article):
	#app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
	app.article.create(article)
	#app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	#app.article.check(Article(title=testdata['testTitle'], note=testdata['testNote']))
	app.article.check(article)
