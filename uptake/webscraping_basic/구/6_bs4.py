import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # attribute(a element 가 가지고 있는 속성 정보 출력)
# print(soup.a["href"]) # a element 의 href '값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 "a" element 를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 "어떤" element 를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})

# 태그간 이동
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling # 다음 element(형제 element) 로 넘어감
# rank3 = rank2.next_sibling.next_sibling 
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # 다음 element(형제 element) 로 넘어감
# print(rank2.a.get_text())
# print(rank1.parent) # rank1 기준 부모 객체로 이동
# rank2 = rank1.find_next_sibling("li") # 다음 element(형제 element) 중 조건("li")에 해당하는 부분만 찾음
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") # 이전 element(형제 element) 중 조건("li")에 해당하는 부분만 찾음
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

# webtoon = soup.find("a", text="랜덤채팅의 그녀!-220. 거짓말쟁이")



print("금일 네이버 웹툰 실시간 순위")
rank_lst = ["rank01", "rank02", "rank03", "rank04", "rank05", "rank06", "rank07", "rank08", "rank09", "rank10"]
for idx, webtoon_title in enumerate(rank_lst):
    rank = soup.find("li", attrs={"class":webtoon_title})
    title = rank.a["title"]
    print(str(idx+1) + "위 -", title)