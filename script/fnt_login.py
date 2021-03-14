

driver.get(url+'/crowd/console/login.action')
driver.implicitly_wait(3)

driver.find_element_by_id('j_username').send_keys(username)
driver.find_element_by_id('j_password').send_keys(userpassword)
driver.find_element_by_id('form-container').submit()

