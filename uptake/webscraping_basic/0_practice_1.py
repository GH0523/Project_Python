# 요일별 웹툰 검색 및 목록 출력

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

def webtoon_finder():
    for idx, webtoon_title in enumerate(webtoon):
        title = webtoon_title.find("a", attrs={"class":"title"})
        print(str(idx+1), "-", title.get_text())


weekday = input("요일 입력(한글자) : ")
if weekday == "월":
    print("\"{0}요일\" 웹툰 목록".format(weekday))
    webtoon = soup.find("h4", attrs={"class":"mon"}).find_next_sibling("ul").find_all("li")
    webtoon_finder()
    
elif weekday == "화":
    print("\"{0}요일\" 웹툰 목록".format(weekday))
    webtoon = soup.find("h4", attrs={"class":"tue"}).find_next_sibling("ul").find_all("li")
    webtoon_finder()

elif weekday == "수":
    print("\"{0}요일\" 웹툰 목록".format(weekday))
    webtoon = soup.find("h4", attrs={"class":"wed"}).find_next_sibling("ul").find_all("li")
    webtoon_finder()

elif weekday == "목":
    print("\"{0}요일\" 웹툰 목록".format(weekday))
    webtoon = soup.find("h4", attrs={"class":"thu"}).find_next_sibling("ul").find_all("li")
    webtoon_finder()

elif weekday == "금":
    print("\"{0}요일\" 웹툰 목록".format(weekday))
    webtoon = soup.find("h4", attrs={"class":"fri"}).find_next_sibling("ul").find_all("li")
    webtoon_finder()

elif weekday == "토":
    print("\"{0}요일\" 웹툰 목록".format(weekday))
    webtoon = soup.find("h4", attrs={"class":"sat"}).find_next_sibling("ul").find_all("li")
    webtoon_finder()

elif weekday == "일":
    print("\"{0}요일\" 웹툰 목록".format(weekday))
    webtoon = soup.find("h4", attrs={"class":"sun"}).find_next_sibling("ul").find_all("li")
    webtoon_finder()

# 그동안 for문의 리스트 항목 변수를 지역변수로 사용했음
# webtoons를 그대로 get_text() 해서 출력하기에는 "NEW", "휴재" 등의 필요없는 정보까지 출력