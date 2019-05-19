from fixture.application import Application
import pytest
import time

testLogin = 'test_user'
testPassword = '12345'


fixture = None

@pytest.fixture()
def app(request):
	'''
	Интеллектуальная фикстура, с проверкой валидности. 
	Создает одну сессию для всех тестов без scope = 'session'
	'''
	global fixture
	if fixture is None: # При первом запуске - из глобальной переменной
		fixture = Application()
		fixture.session.login(username = testLogin, password = testPassword)
	else:
		if not fixture.is_valid(): # Если упала, то в методе application.Application получаем False
			fixture = Application()
			fixture.session.login(username = testLogin, password = testPassword)
	return fixture
			
@pytest.fixture(scope = 'session', autouse = True)
def stop(request):
	'''
	Завершаем браузер в конце тестов.
	'''
	def fin():
		#fixture.session.logout()
		fixture.destroy()
	request.addfinalizer(fin)
	return fixture

