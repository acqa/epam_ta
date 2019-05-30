import pytest

@pytest.mark.smoke_test
def test_create_article(app, data_one_articles):
	article = data_one_articles
	app.article.create(article)
	# add assert

@pytest.mark.run_these_please
def test_check_article(app, data_one_articles):
	article = data_one_articles
	app.article.create(article)
	app.article.check(article)
	# add assert