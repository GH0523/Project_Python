# 디스코드 로그인 및 텍스트 전송 자동화

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Users\\USER\\Desktop\\Python 3.9\\PythonWorkspace\\uptake\\webscraping_basic\\chromedriver.exe")
browser.maximize_window()
url = "https://discord.com/login"
browser.get(url)

text_id = input("이메일 또는 전화번호 입력 : ")
text_pw = input("비밀번호 입력 : ")

browser.find_element_by_name("email").send_keys(text_id)
browser.find_element_by_name("password").send_keys(text_pw)
browser.find_element(By.XPATH, '//div[text() = "로그인"]').click()

pyautogui.sleep(5)

img_server = pyautogui.locateOnScreen("img_server.png", confidence=0.9)
pyautogui.click(img_server)

text = input("전송할 메시지 입력 : ")
index = input("전송할 횟수 입력 : ")

idx = 0
for i in range(int(index)):
    elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div")
    elem.send_keys(text)
    elem.send_keys(Keys.ENTER)
    idx += 1
    print("{0}회 전송중...".format(idx))
    pyautogui.sleep(3)

print("{0}회 전송 완료".format(idx))

exit()