import time
from model.article import Article
import random
import string

def random_string(prefix, maxlen):
	'''
	Генератор случайных строк случайно длины, но не больше заданной
	'''
	symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
	return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata0 = [
	Article(title = 'First title', note = 'First note'),
	Article(title = 'Empty note', note = ''),
	Article(title = '', note = 'Empty title'),
	Article(title = random_string("Tilte ", 10), note = random_string("Note ", 20))
]

testdata4 = [
	Article(title = title, note = note)
	for title in ["", random_string("Tilte ", 10)]
	for note in [random_string("Note ", 20)]
]

testdata_random = [
	Article(title = 'Random Tilte', note = 'Random Note')
	] + [
	Article(title = random_string("Tilte ", 10), note = random_string("Note ", 20)) for i in range(2)
	]
	

testdata_static = [
	Article(title = 'First title', note = 'First note'),
	Article(title = 'Empty note', note = ''),
	Article(title = '', note = 'Empty title'),
	Article(title = 'Текущее время ' + str(time.time()), note = 'Тестовая запись ' + str(time.localtime()))

]