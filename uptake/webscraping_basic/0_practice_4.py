# 네이버 이미지 검색 및 다운로드

# import requests
# from bs4 import BeautifulSoup

# url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EB%B8%8C+%EB%A0%88%EC%9D%B4"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# images = soup.find_all("div", attrs={"class":"tile_item _item"})
# print(len(images))

# 네이버에서 이미지 탭으로 이동시 로딩시간 때문에 아무것도 불러오지 못하는 것으로 추측됨
# selenium을 통해서 시도

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

text = input("찾을 이미지 입력 : ")

browser = webdriver.Chrome()
url = "https://www.naver.com/"
browser.get(url)

browser.find_element_by_id("query").send_keys(text)
browser.find_element_by_class_name("ico_search_submit").click()
browser.find_element(By.XPATH, '//a[text() = "이미지"]').click()

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//img[@class="_image _listImage"]')))

import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, "lxml") 

images = soup.find_all("div", attrs={"class":"tile_item _item"})

for idx, image in enumerate(images):
    image_url = image.find("img", attrs={"class":"_image _listImage"})["src"]
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("{0}_{1}.jpg".format(text.replace(" ", "_"), idx+1), "wb") as f:
        f.write(image_res.content)

    if idx >= 4:
        break

print("이미지 다운로드 완료")

browser.quit()



# input()