import time
from selenium import webdriver
from selenium.webdriver.common.by import By # xpath를 통해 검색하기 위한 import
from selenium.webdriver.support.ui import WebDriverWait # 특정 엘리먼트가 나올때 까지 기다리도록 하기 위한 import
from selenium.webdriver.support import expected_conditions as EC # 기다리는 조건 정의를 위한 import

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str))) # WebDriverWait의 def를 통한 함수화

browser = webdriver.Chrome()
url = 'https://flight.naver.com/'
browser.get(url)

begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

# time.sleep(1) # "가는 날" 클릭 후, 날짜 테이블을 불러오기까지의 약간의 시간차에 의해 오류 발생 가능
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "3"]'))) # >>> 또는 아래에서 사용한 WebDriverWait 활용
day3 = browser.find_elements(By.XPATH, '//b[text() = "10"]')
day3[0].click()

day5 = browser.find_elements(By.XPATH, '//b[text() = "15"]')
day5[0].click()

arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

# time.sleep(1)
wait_until('//button[text() = "국내"]') # WebDriverWait의 def를 통한 함수화 활용
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]') 
jeju.click()

search = browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]') 
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
# ^^^            브라우저를, 30초 동안 기다린다                                      해당 엘리먼트가 나올 때 까지
# 만약 부여된 조건의 시간이 지나도 엘리먼트가 나타나지 않을 경우 오류 출력(try문을 통해 플랜B로 가는 작업도 가능)
print(elem.text)

browser.quit()