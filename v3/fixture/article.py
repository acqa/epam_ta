from selenium.webdriver.common.keys import Keys

class ArticleHelper:

	def __init__(self, app):
		self.app = app # 

	def create(self, articleTitle, articleText):
		wd = self.app.wd
		wd.find_element_by_id('menu-posts').click()
		wd.find_element_by_link_text('Добавить новую').click()
		wd.find_element_by_xpath("//button[@aria-label = 'Отключить советы']").click()
		wd.find_element_by_id('post-title-0').send_keys(articleTitle + Keys.TAB + Keys.TAB + Keys.TAB)
		wd.find_element_by_xpath('//p[@role="textbox"]').send_keys(articleText)
		wd.find_element_by_xpath("//*[text() ='Опубликовать...']").click()
		wd.find_element_by_xpath("//*[text() ='Опубликовать']").click()

	def check(self, articleTitle, articleText):
		wd = self.app.wd
		wd.find_element_by_link_text(articleTitle).click()
		self.textSite = wd.find_element_by_xpath("//div[@class='entry-content']")
		self.actualNote = self.textSite.get_attribute('innerText')
		assert self.actualNote == articleText

