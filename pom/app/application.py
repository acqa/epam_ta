from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from fixture.session import SessionHelper
# from fixture.article import ArticleHelper
# from fixture.comment import CommentHelper
#

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.post_page import PostPage


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
		self.session = Session(self)
		# self.article = ArticleHelper(self)
		# self.comment = CommentHelper(self)
		self.base_url = base_url
		self.base_page = BasePage(self)
		self.home_page = HomePage(self)
		self.login_page = LoginPage(self)
		self.post_page = PostPage(self)


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



class Session(LoginPage):

	def __init__(self, app):
		self.app = app #

	# def login(self, username, password):
	# 	wd = self.app.wd
	# 	self.app.open_login_page()
	# 	time.sleep(1)
	# 	loginField.send_keys(username)
	# 	passField.send_keys(password)
	# 	submitButton.click()
	# 	self.app.open_new_post_page()
	# 	wd.find_element_by_xpath("//button[@aria-label = 'Отключить советы']").click()

	def login(self, username, password):
		wd = self.app.wd
		# self.app.open_home_page()
		# try:
		# 	wd.find_element_by_link_text('Selenium TA site').send_keys(Keys.PAGE_DOWN)
		# 	wd.find_element_by_link_text('Войти').click()
		# except: self.app.open_login_page()
		self.app.open_login_page()
		time.sleep(1)
		wd.find_element_by_id('user_login').send_keys(username)
		wd.find_element_by_id('user_pass').send_keys(password)
		wd.find_element_by_id('wp-submit').click()
		self.app.open_new_post_page()
		# wd.find_element_by_id('menu-posts').click()
		# wd.find_element_by_link_text('Добавить новую').click()
		wd.find_element_by_xpath("//button[@aria-label = 'Отключить советы']").click()
		# self.app.open_home_page()


	def logout(self):
		wd = self.app.wd
		self.app.open_home_page()
		#time.sleep(1)
		wd.find_element_by_link_text('Selenium TA site').send_keys(Keys.PAGE_DOWN)
		wd.find_element_by_link_text('Выйти').click()
		wd.find_element_by_xpath('//*[@id="backtoblog"]/a')
