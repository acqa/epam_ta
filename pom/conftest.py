from app.application import App
import pytest
import os.path
import time
import os


#testdata
base_url = "http://v999140x.beget.tech"
login ="test_user"
password ="12345"

@pytest.fixture(scope = 'session')
def app(request):
	fixture = App(base_url = base_url)
	fixture.login_page.fix_login(login = login, password = password)
	fixture.post_page.fix_close_advice_popup()
	yield fixture
	fixture.destroy()





# @pytest.fixture(scope="function", autouse=True)
# def take_screenshot_when_failure(request):
#
# 	def tear_down():
# 		path = os.path.dirname(__file__)
# 		# if request.node.rep_call.failed:
# 		fixture.wd.save_screenshot("%s/log/screen/scr_%s.png" % (path, time.time()))
# 	request.addfinalizer(tear_down)
# 	yield

# @pytest.fixture(autouse=True, scope="function")
# def screenshot_on_failure(request):
#     def fin():
#         driver = App(base_url = base_url)
#         attach = driver.get_screenshot_as_png()
#         if request.node.rep_setup.failed:
#             allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
#         elif request.node.rep_setup.passed:
#             if request.node.rep_call.failed:
#                 allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
#     request.addfinalizer(fin)


@pytest.fixture(autouse=True, scope='session')
def generate_allure_report():
    """Генерирует HTML отчет из результатов теста"""
    yield
    os.system("allure generate -c ../log/allure/result -o ../log/allure/report")




@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Сообщает время в конце session(сеанса)."""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')

@pytest.fixture(autouse=True)
def footer_function_scope():
    """Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))