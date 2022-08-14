import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"}) # >>> list 형태 (+ find : 조건에 해당하는 첫번째 엘리먼트, find_all : 조건에 해당하는 모든 엘리먼트)
# a 엘리먼트의, class 속성이 title 인 모든 엘리먼트 반환
for cartoon in cartoons:
    print(cartoon.get_text())