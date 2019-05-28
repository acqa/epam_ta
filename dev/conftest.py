from fixture.application import Application
import pytest
import json
import os.path


fixture = None
target = None

@pytest.fixture()
def app(request):
	'''
	Интеллектуальная фикстура, с проверкой валидности. 
	Создает одну сессию для всех тестов без scope = 'session'
	Переработана
	'''
	global fixture
	global target
	browser = request.config.getoption('--browser') # Задаем название браузера в опции командной строки
	if target is None:
		# Определяем текущую директорию файла conftest.py
		config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
		with open(config_file) as f: # Загружаем конфиг. файл
			target = json.load(f)
	if fixture is None or not fixture.is_valid(): # При первом запуске - из глобальной переменной
		fixture = Application(browser = browser, base_url = target["baseUrl"])
		fixture.session.login(username = target["username"], password = target["password"])
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

def pytest_addoption(parser):
	'''
	Функция pytest-а для добавления опций в командной строке
	'''
	parser.addoption('--browser', action = 'store', default = 'chrome') # выбор браузера
	parser.addoption('--target', action = 'store', default = 'target.json') # загрузка параметров из конфиг. файла

