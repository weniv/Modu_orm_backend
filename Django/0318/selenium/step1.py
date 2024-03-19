# playwright와 같은 대체재가 있습니다. 요즘 주목 받고 있으니 한 번 사용해보시길 권해드립니다.
# pip install webdriver_manager와 같은 패키지를 설치하면 더 편리하게 셀레니움을 사용할 수 있습니다.
# 참고 블로그 글: https://velog.io/@dlalscjf94/Python-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%8B%9C-%EB%A7%A4%EC%9A%B0-%EC%9C%A0%EC%9A%A9%ED%95%9C-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%ACwebdrivermanager

from selenium import webdriver

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome()

# 브라우저의 위치를 조정합니다. 수업용으로 세팅해놓은 것입니다.
driver.set_window_position(2000, 0)

# webdriver가 google 페이지에 접속하도록 명령
driver.get("https://www.google.com")

# webdriver를 종료하여 창이 사라진다
driver.close()
