'''
Тестовое задание

1. Установить у себя локально wordpress (изучить как это сделать)
2. Написать тест, позволяющий пользователю залогинится на сайт
3. Написать тест для добавления статьи на сайт
4. Проверить, что статья успешно добавлена и соотвествует тому, что было указано в пункте 3

Необходимо использовать:
xpath, maven, testng, java

это домашнее задание

код нужно выложить в github

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


wd = webdriver.Chrome()
#wd = webdriver.Firefox()
#wd = webdriver.Safari()

# Тестовые данные
testUrl = 'http://v999140x.beget.tech'
testLogin = 'test_user'
testPassword = '12345'
testTitle = 'Текущее время ' + str(time.time())
testNote = 'Тестовая запись ' + str(time.localtime())


# Авторизация на сайте
wd.get(testUrl)
#wd.find_element_by_link_text('Войти').click()
#time.sleep(2)
#wd.find_element_by_xpath("//a[text() = 'Войти']").click()
wd.get(testUrl + '/wp-login.php')
time.sleep(1)
wd.find_element_by_id('user_login').send_keys(testLogin)
wd.find_element_by_id('user_pass').send_keys(testPassword)
wd.find_element_by_id('wp-submit').click()

loginProof = wd.find_element_by_xpath("//div[contains(text(), 'Профиль')]")
loginProofAtt = loginProof.get_attribute('innerText')
assert loginProofAtt == 'Профиль'

# if loginProofAtt == 'Профиль':
#   print()
#   print('Авторизация успешная. Находимся в админ. панели.')


# Создание новой статьи
wd.find_element_by_id('menu-posts').click()
wd.find_element_by_link_text('Добавить новую').click()
wd.find_element_by_xpath("//button[@aria-label = 'Отключить советы']").click()
wd.find_element_by_id('post-title-0').send_keys(testTitle + Keys.TAB + Keys.TAB + Keys.TAB)
wd.find_element_by_xpath('//p[@role="textbox"]').send_keys(testNote)
wd.find_element_by_xpath("//*[text() ='Опубликовать...']").click()
wd.find_element_by_xpath("//*[text() ='Опубликовать']").click()

time.sleep(3)

#wd.find_element_by_xpath("//a[@class = 'components-button is-button is-default']").click()
#wd.find_element_by_link_text(testTitle).click()

# Проверка наличия созданной статьи
wd.get(testUrl)
wd.find_element_by_link_text(testTitle).click()
textSite = wd.find_element_by_xpath("//div[@class='entry-content']")
actualNote = textSite.get_attribute('innerText')
#print(type(text), text)
assert actualNote == testNote
if actualNote == testNote:
  print()
  print('Статья соответствует заданной.')
else: 
  print()
  print('Ошибка! Статья на сайте отличается от заданной.')

# Завершение процесса браузера
wd.quit()
