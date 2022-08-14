import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline > 공백으로 둚으로서 각 줄 마다 줄바꿈을 제거 해줌 / utf8 > 액셀 내 글자가 깨져 utf-8-sig 로 설정
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")

writer.writerow(title) # writerow > list 형식만 들어감

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 불필요한 데이터(페이지 내 줄간격 등) 제외 처리
            continue
        data = [column.get_text().strip() for column in columns] # .strip() > 불필요한 정보 제외하기 위한 함수
        # print(data)
        writer.writerow(data)