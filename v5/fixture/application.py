from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fixture.session import SessionHelper
from fixture.article import ArticleHelper
from fixture.comment import CommentHelper

class Application:
	'''
	Слой вспомогательных методов
	'''
	def __init__(self):
		'''
		Конструктор инициализации драйвера и помощников
		'''
		self.wd = webdriver.Chrome()
		self.wd.implicitly_wait(10)
		self.session = SessionHelper(self)
		self.article = ArticleHelper(self)
		self.comment = CommentHelper(self)

	def is_valid(self):
		try:
			self.wd.current_url
			return True
		except:
			return False

	def open_home_page(self, url = 'http://v999140x.beget.tech'):
		wd = self.wd
		wd.get(url)

	def open_login_page(self, url = 'http://v999140x.beget.tech/wp-login.php'):
		wd = self.wd
		wd.get(url)		

	def open_concole_page(self, url = 'http://v999140x.beget.tech/wp-admin/'):
		wd = self.wd
		wd.get(url)		

	def open_logout_page(self, url = 'http://v999140x.beget.tech/wp-login.php?action=logout'):
		wd = self.wd
		wd.get(url)	


	def destroy(self):
		'''
		Завершение драйвера
		'''
		self.wd.quit()



