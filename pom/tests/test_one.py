import pytest

#testdata
title = 'Title'
note = 'Note'



def test_login(app):
	pass

# def test_navigate_pages(app):
# 	app.home_page.open()
# 	time.sleep(1)
# 	app.admin_page.open()
# 	time.sleep(1)
# 	app.post_page.open()
# 	time.sleep(1)

def test_create_article(app):
	app.post_page.create_article(title = title, note = note)


def test_check_article(app):
	app.post_page.create_article(title = title, note = note)
	actualTitle = app.article_page.titleText()
	actualNote = app.article_page.noteText()
	assert title == actualTitle or note == actualNote


# def test_eggs():
#     assert False