from selenium import webdriver

browser = webdriver.Chrome() # chromedriver 가 다른 경로에 있다면 경로 입력
browser.get("http://naver.com")