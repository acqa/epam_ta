import time
from model.article import Article
import pytest
import random
import string


def random_string(prefix, maxlen):
	'''
	Генератор случайных строк случайно длины, но не больше заданной
	'''
	symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
	return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Test data
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())
testdata = {"testTitle":testTitle, "testNote":testNote}


testdata2 = [
	Article(title = 'First title', note = 'First note'),
	Article(title = 'Empty note', note = ''),
	Article(title = '', note = 'Empty title'),
	Article(title = random_string("Tilte ", 10), note = random_string("Note ", 20))
]

testdata3 = [
	Article(title = 'First title', note = 'First note'),
	Article(title = 'Empty note', note = ''),
	Article(title = '', note = 'Empty title')
	] + [
	Article(title = random_string("Tilte ", 10), note = random_string("Note ", 20)) for i in range(3)
	]
	
testdata4 = [
	Article(title = title, note = note)
	for title in ["", random_string("Tilte ", 10)]
	for note in [random_string("Note ", 20)]
]




@pytest.mark.parametrize("article", testdata3, ids = [repr(x) for x in testdata3])
def test_create_article_param(app, article):
	pass
	##app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	#app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
	app.article.create(article)


def test_create_article(app):
	#app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))


def test_check_article(app):
	app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
	#app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
	app.article.check(Article(title=testdata['testTitle'], note=testdata['testNote']))
