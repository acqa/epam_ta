'''
Данный тест использует параметры из файла data.articles,
которая задается через метод фикстуры
pytest_generate_tests.
Не требует импорта в самом модуле теста.
в параметре data_% - вместо % должно быть имя модуля в пакете data, из которого производится
загрузка тестовых данных фикстурой.
'''

def test_create_article(app, data_articles):
	article = data_articles
	app.article.create(article)
	# add assert


def test_check_article(app, data_for_comments):
	article = data_for_comments
	app.article.create(article)
	app.article.check(article)
	# add assert