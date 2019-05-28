'''
После изменения вспомогательного метода fixture.article.create - данный тест не будет работать
'''

# from model.article import Article
# import pytest
# from data.articles import testdata
# from data.articles import testdata_random
#
#
#
#
#
#
# def test_create_article(app):
# 	app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
# 	# app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
#
#
#
#
# def test_check_article(app):
# 	app.article.create(Article(title=testdata['testTitle'], note=testdata['testNote']))
#
# 	#app.article.create(articleTitle=testdata['testTitle'], articleText=testdata['testNote'])
# 	app.article.check(Article(title=testdata['testTitle'], note=testdata['testNote']))
#
