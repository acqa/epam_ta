
class Article:

    def __init__(self, title, note):
        self.title = title
        self.note = note

    def __repr__(self):
    	'''
    	Используется в test_aritle для вывода значений в параметризации теста
    	'''
    	return "%s:%s" % (self.title, self.note)