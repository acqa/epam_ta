
class PostPage:

    def __init__(self, app):
        self.app = app  #

    def title(self):
        wd = self.app.wd
        title = wd.find_element_by_id('post-title-0')
        return title

    def note(self):



    note = wd.find_element_by_xpath('//p[@role="textbox"]').send_keys(article.note)
    wd.find_element_by_xpath("//*[text() ='Опубликовать...']").click()
    wd.find_element_by_xpath("//*[text() ='Опубликовать']").click()