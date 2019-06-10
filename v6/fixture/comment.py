from selenium.webdriver.common.keys import Keys

class CommentHelper:

	def __init__(self, app):
		self.app = app # 

	def create(self, commentText):
		wd = self.app.wd
		self.app.open_home_page()
		wd.find_element_by_xpath('//h2[@class="entry-title"]/a').click()
		# wd.find_elements_by_xpath('//h2[@class="entry-title"]/a')[1].click() # Замена вышестоящей сторки, если курсор не в топе страницы
		wd.find_element_by_xpath("//textarea").click()
		wd.find_element_by_xpath('//*[@id="comment"]').send_keys(commentText + Keys.TAB)
		wd.find_element_by_xpath('//*[@id="submit"]').click()
