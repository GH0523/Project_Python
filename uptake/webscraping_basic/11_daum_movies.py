import requests
from bs4 import BeautifulSoup

for year in range(2017, 2021):
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"): # https: 가 없는 정보도 출력되어 조건문 추가(.startswith)
            image_url = "https:" + image_url

        # url 접속 및 파일 저장
        image_res = requests.get(image_url) # url 접속 및 정보 저장하기 위해, requests 이용하여 새롭게 접속
        image_res.raise_for_status()

        with open("movie_{0}_{1}.jpg".format(year, idx+1), "wb") as f: # 상위 for문이 실행됨에 따라 파일명이 같아 덮어씌워지므로 year 정보도 파일명에 추가
            f.write(image_res.content) # .content > resource(여기서는 image_res)가 가지고 있는 content 정보를 파일로 가져옴
        
        if idx >= 4: # 상위 5개 이미지 까지만 다운로드
            break