import time

class SessionHelper:

	def __init__(self, app):
		self.app = app # 

	def login(self, username, password):
		wd = self.app.wd
		self.app.open_login_page()
		# try:
		# 	wd.find_element_by_link_text('Войти').click()
		# except: self.open_login_page()
		time.sleep(1)
		wd.find_element_by_id('user_login').send_keys(username)
		wd.find_element_by_id('user_pass').send_keys(password)
		wd.find_element_by_id('wp-submit').click()

	# def logout(self):
	# 	wd = self.app.wd
	# 	wd.find_element_by_link_text('Выйти').click()