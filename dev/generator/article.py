from model.article import Article
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of articles", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/articles.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":\
        f = a

def random_string(prefix, maxlen):
    '''
    Генератор случайных строк случайно длины, но не больше заданной
    '''
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata_random = [
                      Article(title='Random Tilte', note='Random Note')
                  ] + [
                      Article(title=random_string("Tilte ", 10), note=random_string("Note ", 20)) for i in range(2)
                  ]

testdata = [
                      Article(title='Random generated Tilte', note='Random Note')
                  ] + [
                      Article(title=random_string("Tilte ", 10), note=random_string("Note ", 20)) for i in range(n)
                  ]


# Определяем путь к файлу тестовых данных. .. - зайти в корневой каталог файла и зайти к каталог, указанный в переменной f
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# with open(file, "w") as out:
#     # т.к. json не может работать со данными, сформированными нашим методом article.Article, то преобразуем его в
#     # словарь и отформатруем вывод с indent=2
#     out.write(json.dumps(testdata, default = lambda x:x.__dict__, indent = 2))


with open(file, "w") as out:
    # т.к. json не может работать со данными, сформированными нашим методом article.Article, то преобразуем его в
    # словарь и отформатруем вывод с indent=2
    # для более удобной конвертации, а затем расконвертации - используем jsonpickle
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))