

def test_create_article(app, json_articles):
	article = json_articles
	app.article.create(article)

def test_check_article(app, json_articles):
	article = json_articles
	app.article.create(article)
	app.article.check(article)