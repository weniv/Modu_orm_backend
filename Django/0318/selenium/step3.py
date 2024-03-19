from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome()

# 브라우저의 위치를 조정합니다. 수업용으로 세팅해놓은 것입니다.
driver.set_window_position(2000, 0)

# webdriver가 google 페이지에 접속하도록 명령
driver.get("http://127.0.0.1:8000/blog/")

# 아래와 같이 id, pw를 입력하고 로그인 버튼을 누르는 코드를 작성할 수도 있습니다.
# id = driver.find_element(By.ID, "emailInput")
# pw = driver.find_element(By.ID, "passwordInput")

# id.send_keys("")
# pw.send_keys("")

# pw.send_keys(Keys.ENTER)
# Kyes.ENTER, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_UP,
# Keys.BACK_SPACE, Keys.CONTROL, Keys.ALT, Keys.DELETE, Keys.TAB, Keys.SPACE,
# Keys.SHIFT, Keys.EQUALS, Keys.ESCAPE, Keys.HOME, Keys.INSERT, Keys.PAGE_UP,
# Keys.PAGE_DOWN,Keys.F1, Keys.F2, Keys.F3, Keys.F4, Keys.F5, Keys.F6, Keys.F7,
# Keys.F8, Keys.F9 Keys.F10, Keys.F11, Keys.F12
time.sleep(1)
search = driver.find_element(By.ID, "search-input")
search.send_keys("1")
time.sleep(1)

search_btn = driver.find_element(By.ID, "search-btn")
search_btn.click()
time.sleep(3)

# webdriver를 종료하여 창이 사라진다
driver.close()
