from selenium.webdriver.common.keys import Keys
import time

class ArticleHelper:

	def __init__(self, app):
		self.app = app # 

	def create(self, article):
		wd = self.app.wd
		# self.app.open_concole_page()
		# wd.find_element_by_id('menu-posts').click()
		# wd.find_element_by_link_text('Добавить новую').click()
		# #wd.find_element_by_xpath("//button[@aria-label = 'Отключить советы']").click()
		self.app.open_new_post_page()
		wd.find_element_by_id('post-title-0').send_keys(article.title + Keys.TAB + Keys.TAB + Keys.TAB)
		wd.find_element_by_xpath('//p[@role="textbox"]').send_keys(article.note)
		wd.find_element_by_xpath("//*[text() ='Опубликовать...']").click()
		wd.find_element_by_xpath("//*[text() ='Опубликовать']").click()
		time.sleep(2) # Можно регулировать падение теста в Chrome: При == 0 упадет, == 1 возможно упадет, =< 3 не упадет.
		# wd.find_element_by_xpath("//*[@id='wp-admin-bar-site-name']/a").click()
		

	def check(self, article):
		wd = self.app.wd
		self.app.open_home_page()
		wd.find_element_by_link_text(article.title).click()
		self.textSite = wd.find_element_by_xpath("//div[@class='entry-content']")
		self.actualNote = self.textSite.get_attribute('innerText')
		assert self.actualNote == article.note


	def count(self):
		'''
		Подсчет количества статей на странице
		'''
		wd = self.app.wd
		self.app.open_home_page()
		return len(wd.find_elements_by_xpath('//h2[@class="entry-title"]/a'))
