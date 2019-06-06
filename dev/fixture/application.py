from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fixture.session import SessionHelper
from fixture.article import ArticleHelper
from fixture.comment import CommentHelper
from page import LoginPage


class Application:
	'''
	Слой вспомогательных методов
	'''
	def __init__(self, browser, base_url):
		'''
		Конструктор инициализации драйвера и помощников
		у параметра browser есть дефолтное значение, которое задается при описании опций в conftest.py - def pytest_addoption(parser)
		'''
		if browser == 'chrome':
			self.wd = webdriver.Chrome()
		elif browser == 'firefox':
			self.wd = webdriver.Firefox()
		else:
			raise ValueError("Unrecognized browser %s" % browser)
		self.wd.implicitly_wait(10)
		self.session = SessionHelper(self)
		self.article = ArticleHelper(self)
		self.comment = CommentHelper(self)
		self.login_page = LoginPage()
		self.base_url = base_url


	def is_valid(self):
		try:
			self.wd.current_url
			return True
		except:
			return False

	def open_home_page(self):
		wd = self.wd
		wd.get(self.base_url)

	def open_login_page(self):
		wd = self.wd
		wd.get(self.base_url + '/wp-login.php')		

	def open_concole_page(self):
		wd = self.wd
		wd.get(self.base_url + '/wp-admin/')		

	def open_new_post_page(self):
		wd = self.wd
		wd.get(self.base_url + '/wp-admin/post-new.php')


	def destroy(self):
		'''
		Завершение драйвера
		'''
		self.wd.quit()



