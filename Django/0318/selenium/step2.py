from selenium import webdriver
from selenium.webdriver.common.by import By

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome()

# 브라우저의 위치를 조정합니다. 수업용으로 세팅해놓은 것입니다.
driver.set_window_position(2000, 0)

# webdriver가 google 페이지에 접속하도록 명령
driver.get("https://www.naver.com")

# 검색 입력 부분에 커서를 올리고
# 검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
# elem = driver.find_element(By.ID, "input")
elem = driver.find_element(By.CSS_SELECTOR, "#query")

# 입력 부분에 default로 값이 있을 수 있어 비운다
elem.clear()

# 검색어를 입력한다
elem.send_keys("Selenium")

# 검색을 실행한다
elem.submit()

# webdriver를 종료하여 창이 사라진다
driver.close()
