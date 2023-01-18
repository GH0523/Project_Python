# 유미 댄스 무한 반복

import time
from selenium import webdriver

index = 0

browser = webdriver.Chrome()

browser.get("https://www.youtube.com/watch?v=OBD0S2Qdq7U")
time.sleep(2)
browser.find_element_by_xpath("//*[@id='movie_player']/div[29]/div[2]/div[1]/button").click()
browser.find_element_by_xpath("//*[@id='movie_player']/div[29]/div[2]/div[2]/button[10]").click()

while True:
    time.sleep(14)
    browser.find_element_by_xpath("//*[@id='movie_player']/div[29]/div[2]/div[1]/button").click()
    index += 1
    print("{0}회 재생중".format(index))