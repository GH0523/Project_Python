import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    rain_rate = soup.find_all("span", attrs={"class":"weather_left"})
    dust = soup.find("ul", attrs={"class":"today_chart_list"}).find_all("li")

    print(cast)
    print("{0} ({1} / {2})".format(curr_temp, min_temp, max_temp))
    print("강수확률 : {0} / {1}".format(rain_rate[0].get_text(), rain_rate[1].get_text()))
    print(dust[0].get_text().strip())
    print(dust[1].get_text().strip())

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/main/officeList.naver"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"section_list_ranking_press _rankingList"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        print("{0}.".format(idx+1), news.find("a", attrs={"class":"list_tit nclicks('rig.renws2')"}).get_text())
        print("  (링크 : {0})".format(news.find("a")["href"]))        
        # if idx >= 2:
        #     break

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, index 기준 4~7 까지 잘라서 가져옴
        print(sentence.get_text().strip())

    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, index 기준 0~3 까지 잘라서 가져옴
        print(sentence.get_text().strip())

if __name__ == "__main__":
    scrape_weather() # 오늘 날씨 정보 가져오기
    print()
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    print()
    scrape_english() # 오늘의 영어 회화 가져오기