from selenium.webdriver.common.keys import Keys

class CommentHelper:

	def __init__(self, app):
		self.app = app # 

	def create(self, commentText):
		wd = self.app.wd
		wd.find_element_by_xpath("//textarea").click()
		wd.find_element_by_xpath('//*[@id="comment"]').send_keys(commentText + Keys.TAB)
		wd.find_element_by_xpath('//*[@id="submit"]').click()