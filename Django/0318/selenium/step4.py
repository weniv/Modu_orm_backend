from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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

search = driver.find_element(By.ID, "search-input")
search.send_keys("1")

search_btn = driver.find_element(By.ID, "search-btn")
search_btn.click()
time.sleep(3)

# req = driver.page_source
req = driver.page_source.encode("cp949", errors="replace")
# soup = BeautifulSoup(req, 'html.parser', from_encoding='urf-8')
# req.encode('utf-8')
# req.encoding = 'utf-8'
print("hello")
# change = req.encode('utf-8')
# print(change)
# a = change.decode('euc-kr')
# a = change.decode('euc-kr')
# print(a)
soup = BeautifulSoup(req, "html.parser")

print(soup)

l = []
for i in soup.select("h2"):
    l.append(i.text.strip())

print(l)
print("world")

# webdriver를 종료하여 창이 사라진다
driver.close()
