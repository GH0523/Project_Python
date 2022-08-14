import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 가져온 html문서를 lxml를 통해 beautifulsoup 객체로 만든 것 > 즉 soup 변수에 모든 정보가 다 들어있음

# 해당 웹 페이지에 대해 잘 알고있을 경우
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체가 가진 모든 정보 중, "첫 번째로 발견되는" a 엘리먼트에 대한 정보 획득
# print(soup.a.attrs) # attrs = 속성 > a 엘리먼트가 가진 속성 정보를 불러옴
# print(soup.a["href"]) # a 엘리먼트 속성 중 href 값을 가져옴

# 대상 페이지에 대한 정보가 별로 없을 경우
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 조건에 해당되며, 처음으로 발견되는 a 엘리먼트의 정보 출력 > soup.find("태그명", 조건)
# print(soup.find(attrs={"class":"Nbtn_upload"})) # 조건에 해당되는 엘리먼트 검색

# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling) # 엘리먼트 사이의 줄바꿈 등에 의해 빈 정보가 뜬 것
# rank2 = rank1.next_sibling.next_sibling # 그렇기에 next_sibling 을 두 번 사용
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # next_sibling 을 두 번 사용하지 않고 "li" 라는 조건을 달아 검색
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

print(rank1.find_next_siblings("li")) # siblings > 모든 형제 엘리먼트 정보를 가져옴