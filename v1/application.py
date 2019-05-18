from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Application:
	'''
	Слой вспомогательных методов
	'''
	def __init__(self):
		self.wd = webdriver.Chrome()
		self.wd.implicitly_wait(60)

	def open_home_page(self, url = 'http://v999140x.beget.tech'):
		wd = self.wd
		wd.get(url)

	def open_login_page(self, url = 'http://v999140x.beget.tech/wp-login.php'):
		wd = self.wd
		wd.get(url)		

	def login(self, username, password):
		wd = self.wd
		self.open_home_page()
		try:
			wd.find_element_by_link_text('Войти').click()
		except: self.open_login_page()
		time.sleep(1)
		wd.find_element_by_id('user_login').send_keys(username)
		wd.find_element_by_id('user_pass').send_keys(password)
		wd.find_element_by_id('wp-submit').click()

	def create_article(self, articleTitle, articleText):
		wd = self.wd
		wd.find_element_by_id('menu-posts').click()
		wd.find_element_by_link_text('Добавить новую').click()
		wd.find_element_by_xpath("//button[@aria-label = 'Отключить советы']").click()
		wd.find_element_by_id('post-title-0').send_keys(articleTitle + Keys.TAB + Keys.TAB + Keys.TAB)
		wd.find_element_by_xpath('//p[@role="textbox"]').send_keys(articleText)
		wd.find_element_by_xpath("//*[text() ='Опубликовать...']").click()
		wd.find_element_by_xpath("//*[text() ='Опубликовать']").click()

	def check_article(self, articleTitle, articleText):
		wd = self.wd
		wd.find_element_by_link_text(articleTitle).click()
		self.textSite = wd.find_element_by_xpath("//div[@class='entry-content']")
		self.actualNote = self.textSite.get_attribute('innerText')
		assert self.actualNote == articleText
	
	# def logout(self):
	# 	wd = self.wd
	# 	wd.find_element_by_link_text('Выйти').click()

	def destroy(self):
		self.wd.quit()



