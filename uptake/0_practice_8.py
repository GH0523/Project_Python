import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until(xpath_str):
    WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome("C:\\Users\\USER\\Desktop\\Python 3.9\\PythonWorkspace\\uptake\\webscraping_basic\\chromedriver.exe")
browser.maximize_window()
url = "https://instagram.com"
browser.get(url)

user_id = input("전화번호, 사용자 이름 또는 이메일 : ")
user_pw = input("비밀번호 : ")
# user_tag = input("유저 닉네임 입력 : ")

browser.find_element_by_name("username").send_keys(user_id) 
browser.find_element_by_name("password").send_keys(user_pw)
browser.find_element(By.XPATH, '//div[text() = "로그인"]').click()

wait_until('//button[text() = "나중에 하기"]')
browser.find_element(By.XPATH, '//button[text() = "나중에 하기"]').click()
wait_until('//button[text() = "나중에 하기"]')
browser.find_element(By.XPATH, '//button[text() = "나중에 하기"]').click()
# browser.find_element(By.XPATH, "//a[text() = user_tag]").click()
browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/section/div[3]/div[1]/div/div/div[1]/div/a/img").click()
wait_until('//div[text() = "팔로우 "]')
browser.find_element(By.XPATH, '//div[text() = "팔로우 "]').click()
wait_until('//div[text() = "팔로잉"]')

index = 1
while True:
    rows = browser.find_elements(By.CSS_SELECTOR, "div[class = '_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm']")
    browser.execute_script("arguments[0].scrollIntoView()", rows[len(rows)-1])
    index += 1
    time.sleep(1)
    if index == 40: # 팔로잉 200 기준 20회 스크롤 다운
        break

print("팔로잉 정보 로딩 완료")

id_follow = browser.find_elements(By.CSS_SELECTOR, "div[class = ' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm']")

no_follow = 215 # 팔로우 수 입력

print("예상 시간 : {0}초".format(str(int(no_follow)*5)))

index = 1
while True:
    id_follow[index-1].click()
    time.sleep(1.5)
    following = browser.find_element(By.CSS_SELECTOR, "h2[class = '_aacl _aacs _aact _aacx _aada']").text
    wait_until('//div[text() = "팔로우 "]')
    browser.find_element(By.XPATH, '//div[text() = "팔로우 "]').click()
    wait_until('//div[text() = "man_gh_0523"]') # 본인 태그 입력
    followed = browser.find_element(By.XPATH, '//div[text() = "man_gh_0523"]')
    time.sleep(1.5)
    if followed:
        print("{0}. {1} : O".format(str(index), following))
    else:
        print("{0}. {1} : X".format(str(index), following))
    browser.back()
    browser.back()    
    time.sleep(1.5)
    id_follow = browser.find_elements(By.CSS_SELECTOR, "div[class = ' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm']")
    index += 1

    if index == int(no_follow):
        break

print("팔로우 여부 확인 완료")



input()


# 6명 확인 후 refresh()