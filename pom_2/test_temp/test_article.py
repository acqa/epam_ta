import pytest

@pytest.mark.smoke_test
def test_create_article(app, data_one_articles):
	# GIVEN получили тестовые данные из файла
	article = data_one_articles
	# WHEN создаем заментку с этими данными
	app.article.create(article)
	# THEN заментка создалась
	# add assert

@pytest.mark.run_these_please
def test_check_article(app, data_one_articles):
	# GIVEN получили тестовые данные из файла
	article = data_one_articles
	# WHEN создаем заментку с этими данными
	app.article.create(article)
	# THEN заметка создалась с заданными тестовыми данными
	app.article.check(article)
	# add assert