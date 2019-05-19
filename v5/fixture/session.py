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
		self.app.open_logout_page()
		wd.find_element_by_link_text('выйти').click()
		self.app.open_home_page()

	def is_logged_in(self):
		wd = self.app.wd
		self.app.open_home_page()
		wd.find_element_by_link_text('Selenium TA site').send_keys(Keys.PAGE_DOWN)
		return len(wd.find_elements_by_link_text('Выйти')) > 0

	def is_logged_in_as(self, username):
		wd = self.app.wd
		self.app.open_home_page()
		wd.find_element_by_link_text('Selenium TA site').send_keys(Keys.PAGE_DOWN)
		return wd.find_element_by_xpath('//*[@id="wp-admin-bar-user-info"]/a/span[2]').text == username

	def ensure_logot(self):
		wd = self.app.wd
		if self.is_logged_in():
			self.logout()

	def ensure_login(self, username, password):
		wd = self.app.wd
		if self.is_logged_in():
			return
			# if self.is_logged_in_as(username):
			# 	return
			# else:
			# 	self.logout()
		self.login(username, password)





