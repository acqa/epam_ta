from model.article import Article

# START Uses for dev/tests/test_article_fixture_param.py
testdata = [
	Article(title = 'First title', note = 'First note'),
	Article(title = 'Empty note', note = ''),
	Article(title = '', note = 'Empty title')
]
# END
