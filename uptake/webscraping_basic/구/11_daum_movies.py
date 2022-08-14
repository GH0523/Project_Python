import requests
from bs4 import BeautifulSoup


for year in range(2017, 2022): # 5. 범위(2017 ~ 2021) 설정
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images): # 1. url 등을 가져온 후 for문 작성
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url) # 2. 출력된 url 에 접속 해서 페이지의 정보를 파일로 저장하기 위해 requests 를 이용해 다시 새롭게 접속하는 과정
        image_res.raise_for_status()

        with open("movie_{0}_{1}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content) # 3. 접속한 url 의 내용 저장

        if idx >= 4: # 4. 상위 5개 이미지 까지만 다운로드
            break



# 짚고 넘어가기
# .startswith (13번 줄)
# .content (21번 줄) > 이 리소스가 가지고 있는 content 정보를 바로 파일로 씀
#  enumerate 의 활용