# THAAD

import random
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

browser.find_element(By.XPATH, '//div[text() = "도박장"]').click() # 억제기

name = input("대상 입력 : ")
text = f"{name} 보지에 전기차충전용 dc콤보꼽아서 충전시킨다음 자동으로 벌렁벌렁 거리게 만든다음 홍등가 유리앞에 전시시켜놓으면 물 존나나와서 전세계 홍수터지고 물부족현상 해결", \
        f"{name} 보지에 군대에서 쓰는 500리터 말통넣고 보짓물받아와서 당근마켓에 1리터당 5백원에팔면 때부자됨. 거의 황금알 낳는 거위.", \
        f"{name} 씹물보지 그냥 산불 났을때 소방헬기 밑에 밧줄로 묶어놓고 미리 넣어둔 진동기 작동하면 미친물보지 분수 퐝 터져서 아주 무지개 그리면서 불 꺼짐", \
        f"{name} 수북한 보지털 예초기로 마구잡이로 휘갈긴다음 까끌까끌한 보지털로 효목골막창에서 하루종일 타서 눌러붙은 냄비들 소까보털 수세미 대용으로 퐁퐁도 필요없이 보짓물로 깨끗이 세척", \
        f"{name} 보지는 220v한국식 전압 사용하는데 실수인척하고 일본에서쓰는 110v짜리 충전기꽂아서 전기통하게했는데 존나걸레년이 그거느끼고서는 전기없이 살지못하는 해파리보지인생됨", \
        f"{name} 보지에 슈팅스타 아이스크림 존나 쳐놓고 보지펀치 한방 날렷더니 아주 안에서 폭죽 펑펑 터지는 소리와 함께 달콤한 씹물보지 줄줄 새어나와서 탕수육 찍먹", \
        f"{name} 보지에 하이마트 마냥 전자매장 오픈해서 냉장고 비스포크, 티비 아이폰 세탁기 건조기 등 각종 물품 판매하는 매장 만들기", \
        f"{name} 클리에 손가락 딱 대고 존나문질렀는대 아무 반응없어서 초록색 때타올 들고와서 손에끼우고 클리문지르니까 봇물이 봇물터지듯나와서 촬영해서 폰허브에 업로드하니까 most viwed 1위 달성", \
        f"{name} 보릉내를 어떻게하면 판매할수있을까 고민하다가 그냥 파리 에펠탑앞에 헨타이식으로 묶어서 누구나 맡아볼수있게만들어놓기",\
        f"유튜브에 꽃에 욕해서 시들게하는 동영상 참고해서 {name} 보지 놔두고 욕하는 영상 찍어서 보지 검은색으로 변해가는 영상 촬영해서 유튜브에 업로드하면 조회수 5조5억 바로 달성",\
        f"{name} 씹보지구녕에 조그만한 콩 놔두고 대한민국 양궁 선수들 불러와서 쏘게 만들었더니 클리랑 콩이랑 헷갈려서 클리 터짐",\
        f"{name} 보지안에다가 공유기설치해서 데이터 다쓸때마다 누구나 사용가능한 보이파이존 만들어서 대구 신세계백화점앞에 만들어놓기",\
        f"신천 산책갔다가 유독 한 분수만 존나 높이 뿜길래 유심히 봤더니 {name} 물구나무서서 클리 문질대고있는 광경보고 지나가는 사람들 전부 구경",\
        f"{name} 개보지에 손흥민 파워슈팅 꽂았더니 탄탄한 탄력고무 보지라 튕겨나온 공이 더 쌔서 손흥민 그거보고 현타와서 축구 접음"
index = input("전송할 횟수 입력 : ")

idx = 0
for i in range(int(index)):
    elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div")
    elem.send_keys(random.choice(text))
    elem.send_keys(Keys.ENTER)
    idx += 1
    print("{0}회 전송중...".format(idx))
    pyautogui.sleep(2)

print("{0}회 전송 완료".format(idx))

exit()