import time

# 계정 등록 여부 확인
def fnt_search_user(driver):
  uconf='search_user.conf'
  user_list=''
  cuser_list=''

  driver.implicitly_wait(3)
  driver.find_element_by_id('topnavBrowseUsers').click()

  f=open(uconf,'r', encoding='utf-8')
  for line in f:
    uname=line.split(" ")[0]
    uid=line.split(" ")[1]
    
    driver.execute_script("javascrit:document.querySelector('#react-container input[name=search]').value=''")
    time.sleep(0.1)
    driver.find_element_by_name('search').send_keys(uname)
    driver.find_element_by_css_selector('#react-container .css-1yx6h60').click()
    time.sleep(1)

    # 검색된 사용자 확인 및 분류


  print('확인 계정')
  # 확인된 계정 출력 - 이름 메일

  print('신규 생성 계정')
  # 확인되지 않은 계정 출력 - 이름 메일
    
  f.close()
