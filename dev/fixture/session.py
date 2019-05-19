import time
from selenium.webdriver.common.keys import Keys

class SessionHelper:

	def __init__(self, app):
		self.app = app # 

	def login(self, username, password):
		wd = self.app.wd
		self.app.open_home_page()
		try:
			wd.find_element_by_link_text('Selenium TA site').send_keys(Keys.PAGE_DOWN)
			wd.find_element_by_link_text('Войти').click()
		except: self.app.open_login_page()
		time.sleep(1)
		wd.find_element_by_id('user_login').send_keys(username)
		wd.find_element_by_id('user_pass').send_keys(password)
		wd.find_element_by_id('wp-submit').click()

	def logout(self):
		wd = self.app.wd
		self.app.open_home_page()
		time.sleep(1)
		wd.find_element_by_link_text('Selenium TA site').send_keys(Keys.PAGE_DOWN)
		wd.find_element_by_link_text('Выйти').click()
		wd.find_element_by_xpath('//*[@id="backtoblog"]/a')




