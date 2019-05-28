

def test_create_article(app, data_articles):
	article = data_articles
	app.article.create(article)

def test_check_article(app, data_articles):
	article = data_articles
	app.article.create(article)
	app.article.check(article)