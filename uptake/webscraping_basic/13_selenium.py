# 셀레니움 : 웹페이지를 띄워 테스트 가능
import time
from selenium import webdriver

browser = webdriver.Chrome() # 현재는 크롬드라이버가 같은 경로에 있어 ()에 아무 정보도 넣지 않지만, 다른 경로라면 ()에 경로 기입

# 1. 네이버 이동
browser.get("http://naver.com") # 크롬웹드라이버 객체 생성 및 그 브라우저에서 해당 url로 이동하는 것

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. ID, PW 입력
browser.find_element_by_id("id").send_keys("id_fake")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3) # id를 새로 입력하려 했지만 화면전환 사이의 시간차에 의해 불가능. 그런고로 3초 후 실행하기 위한 명령문

# 5. id 새로 입력
# browser.find_element_by_id("id").send_keys("id_mine")
browser.find_element_by_id("id").clear() # 해당 엘리먼트에 입력되어있는 텍스트를 지워줌
browser.find_element_by_id("id").send_keys("id_mine")

# 6. html 정보 출력
print(browser.page_source) # 현재 페이지의 모든 html 문서를 출력

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료

input()


# 터미널에서의 실행 내역

# python
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get("http://naver.com")
# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back() # 뒤로가기
# browser.forward() # 앞으로가기
# browser.refresh() # 새로고침

# elem = browser.find_element_by_id("query") # 검색창 찾기
# elem.send_keys("아무 검색어") # 텍스트 입력
# from selenium.webdriver.common.keys import Keys # 아래 명령어를 위한 import
# elem.send_keys(Keys.ENTER) # 엔터

# elem = browser.find_elements_by_tag_name("a") # elements > 모든 엘리먼트 출력
# for e in element:
#     elem.get_attribute("href") # 이후에도 계속 입력 할 수 있으므로, 실행하려면 엔터 두 번

# elem = browser.find_element_by_xpath("xpath정보") # 터미널에서 우클릭시 붙여넣기 기능
# elem.click()

# browser.close() # 현재 탭 닫기
# browser.quit() # 전체 탭 닫기