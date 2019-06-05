import pytest
from data.articles import testdata_static_1
from data.articles import testdata_random_1
from data.articles import testdata_comment

@pytest.mark.parametrize("article", testdata_random_1, ids = [repr(x) for x in testdata_random_1])
def test_create_article(app, article):
	app.article.create(article)
	# add assert


@pytest.mark.parametrize("article", testdata_comment, ids = [repr(x) for x in testdata_comment])
def test_check_article(app, article):
	app.article.create(article)
	app.article.check(article)
	# add assert