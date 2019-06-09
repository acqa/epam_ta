from app.application import App
import pytest
import json
import jsonpickle
import os.path
import importlib


# fixture = None
# target = None
# target = {
# 	"baseUrl" : "http://v999140x.beget.tech",
# 	"username" : "test_user",
# 	"password" : "12345"
#
# }

base_url = "http://v999140x.beget.tech"


@pytest.fixture(scope = 'session')
def app(request):
	app = App(base_url = base_url)
	app.login_page.fix_login(login ="test_user", password ="12345")
	app.post_page.fix_close_advice_popup()
	yield app
	app.destroy()


# @pytest.fixture(scope = 'session', autouse = True)
# def stop(request):
# 	"""Завершаем браузер в конце тестов.
# 	"""
# 	def fin():
# 		#fixture.session.logout()
# 		app.destroy()
# 	request.addfinalizer(fin)
# 	return app






#
#
#
# @pytest.fixture()
# def app(request):
# 	"""	Интеллектуальная фикстура, с проверкой валидности
# 	Создает одну сессию для всех тестов без scope = 'session'
# 	Переработана
#
# 	"""
# 	global fixture
# 	global target
# 	browser = request.config.getoption('--browser') # Задаем название браузера в опции командной строки
# 	if target is None:
# 		# Определяем текущую директорию файла conftest.py
# 		config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
# 		with open(config_file) as f: # Загружаем конфиг. файл
# 			target = json.load(f)
# 	if fixture is None or not fixture.is_valid(): # При первом запуске - из глобальной переменной
# 		fixture = Application(browser = browser, base_url = target["baseUrl"])
# 		fixture.session.login(username = target["username"], password = target["password"])
# 	return fixture
#
#
#
# @pytest.fixture(scope = 'session', autouse = True)
# def stop(request):
# 	"""Завершаем браузер в конце тестов.
# 	"""
# 	def fin():
# 		#fixture.session.logout()
# 		fixture.destroy()
# 	request.addfinalizer(fin)
# 	return fixture
#
#
# def pytest_addoption(parser):
# 	"""Функция pytest-а для добавления опций в командной строке
# 	"""
# 	parser.addoption('--browser', action = 'store', default = 'chrome') # выбор браузера
# 	parser.addoption('--target', action = 'store', default = 'config/target.json') # загрузка параметров из конфиг. файла
#
#
# def pytest_generate_tests(metafunc):
# 	"""	Функция производит загрузку тестовых данных из файла articles.py в пакете data (задается в тесте)
# 	или из файла articles.json в из того же пакета.
# 	"""
# 	for fixture in metafunc.fixturenames:
# 		if fixture.startswith("data_"):
# 			testdata = load_from_module(fixture[5:])
# 			metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])
# 		elif fixture.startswith("json_"):
# 			testdata = load_from_json(fixture[5:])
# 			metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])
#
#
# def load_from_module(module):
# 	"""Производим загрузку тестовых данных из модуля
# 	"""
# 	return importlib.import_module("data.%s" % module).testdata
#
# def load_from_json(json_file):
# 	"""Производим загрузку тестовых данных из json-файла
# 	"""
# 	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % json_file)) as f:
# 		return jsonpickle.decode((f.read()))
#