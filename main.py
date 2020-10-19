from time import sleep
from selenium import webdriver
browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://www.got-it.ai/solutions/excel-chat/')
login = browser.find_element_by_id('test-login-button')
login.click()
browser.implicitly_wait(10)
email = browser.find_element_by_name('email')
email.click()
email.send_keys('alice.nguyn@gmail.com')
password = browser.find_element_by_name('password')
password.click()
password.send_keys('Excelchat153$$$')
submit = browser.find_element_by_id('login-button')
submit.click()
sleep(10)
result = browser.current_url
if result == 'https://www.got-it.ai/solutions/excel-chat/home':
    print('Success')
browser.close()
