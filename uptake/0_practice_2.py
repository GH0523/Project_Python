# 네이버 인기영화 검색 및 이미지 다운로드

import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("span", attrs={"class", "cm_thumb_rank_number"})

for idx, image in enumerate(images):
    photo = image.find_next_sibling("img")
    image_url = photo["src"]
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("nowadaysmovie_{0}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)

    if idx >= 9:
        break

# 포털사이트(네이버, 다음 등)의 검색 후 메인화면에 있는 정보는 출력이 됨
# 그런데 검색 후 이미지 탭 등, 다른 화면으로 전환 시 정보가 출력되지 않음