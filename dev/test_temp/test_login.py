import time
import pytest


testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())

@pytest.mark.smoke_test
def test_login(app):
	pass
	# add assert
	






		