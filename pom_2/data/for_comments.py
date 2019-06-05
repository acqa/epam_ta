import time
from model.article import Article


# START Uses for test comment in dev/test/test_article_fixture_param.py and dev/test/test_artiicle_parametrize.py
testdata = [
	Article(title='Test comment title ' + str(time.time()), note='Test comment note ' + str(time.localtime()))
]
# END