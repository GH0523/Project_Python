import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", 
    "Accept-Language":"ko-KR,ko"
    } # html 문서 접속시 내 Headers 정보에 따른, 한글로 설정된 국내 페이지를 불러오기 위해

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies)) # 웹페이지가 10개씩 불러오는 형식이라 파이썬에서 10으로 출력됨 > selenium 활용

with open ("movie.html", "w", encoding="utf-8") as f:
    # f.write(res.text)
    f.write(soup.prettify()) # html 문서를 깔끔하게 출력

    # ^^^ 이를 통해 html 파일을 만들어, Headers 정보를 기입해야 하는지, selenium을 활용해야 하는지 판단 가능

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)