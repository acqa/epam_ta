import time
from model.article import Article
import random
import string

# START Uses for dev/test/test_artiicle_parametrize.py
testdata_static_1 = [
	Article(title = 'First title', note = 'First note'),
	Article(title = 'Empty note', note = ''),
	Article(title = '', note = 'Empty title'),
	Article(title = 'Текущее время ' + str(time.time()), note = 'Тестовая запись ' + str(time.localtime()))
]

def random_string(prefix, maxlen):
	'''
	Генератор случайных строк случайно длины, но не больше заданной
	'''
	symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
	return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata_random_1 = [
	Article(title = 'Random Tilte', note = 'Random Note')
	] + [
	Article(title = random_string("Tilte ", 10), note = random_string("Note ", 20)) for i in range(2)
	]
# END



# START Uses for dev/test/test_article_fixture_param.py
testdata = [
	Article(title = 'First title', note = 'First note'),
	Article(title = 'Empty note', note = ''),
	Article(title = '', note = 'Empty title')
]
# END


# START Uses for test comment
testdata_comment = [
	Article(title='Test comment title ' + str(time.time()), note='Test comment note ' + str(time.localtime()))
]
# END