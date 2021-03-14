from selenium import webdriver
from bs4 import BeautifulSoup
import os

conf='crowd_test.conf'
d='chromedriver'
s='script'
path_chromedriver='./'+d+'/chromedriver'
url=''
username=''
userpassword=''

# set web driver
driver = webdriver.Chrome(path_chromedriver)

def init():
  # set config
  f=open(conf,'r', encoding='utf-8')
  for line in f:
    if 'url' in line:
      url=line.split(":'")[1].split("'")[0]
    if 'username' in line:
      username=line.split(":'")[1].split("'")[0]
    if 'password' in line:
      userpassword=line.split(":'")[1].split("'")[0]
  f.close()
  
  try:
    if not(os.path.isdir(d)):
      os.makedirs(os.path.join(d))
      #### added download code
  except OSError as e:
    if e.errno != errno.EEXIST:
      print("Failed to create directory!!!!!")
      raise
  
  driver.implicitly_wait(3)

  # login
  driver.get(url+'/crowd/console/login.action')
  driver.implicitly_wait(3)

  driver.find_element_by_id('j_username').send_keys(username)
  driver.find_element_by_id('j_password').send_keys(userpassword)
  driver.find_element_by_id('form-container').submit()

init()
