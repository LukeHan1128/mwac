from selenium import webdriver
from bs4 import BeautifulSoup

username='crowd'
userpassword='crowd'

path_chromedriver='./chromedriver/chromedriver'
url_crowd='http://192.168.0.100:8095/crowd/console/login.action'

driver = webdriver.Chrome(path_chromedriver)
driver.implicitly_wait(3)
driver.get(url_crowd)
driver.implicitly_wait(3)

driver.find_element_by_id('j_username').send_keys(username)
driver.find_element_by_id('j_password').send_keys(userpassword)
driver.find_element_by_id('form-container').submit()

