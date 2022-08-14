import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # utf8 로는 엑셀 파일 인코딩에 문제가 생겨 utf-8-sig 로 변경
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml") # 페이지 정보를 가져온 후 오류검사 등 실행

    # 데이터 형식이 테이블로 되어있어, 테이블을 가져온 후 그 아래의 tr 정보들을 출력하는 형식으로
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data) # lst 형식으로 된 데이터를 넣어줌

# .strip() > 문자열 좌우 공백 삭제 [.lstrip(), .rstrip()]
# .replace(a, b) > a를 b로 대체(활용하여 공백 삭제 가능)
# .split() > 문자열이 공백을 기준으로 잘라, lst 형태로 변환 (()에는 조건 추가 가능{본문 11줄의 경우 탭(t)으로 잘려있어, .split("\t") 형태로 사용})