import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

# 접속하는 header 정보가 사람이 아닌 컴퓨터가 접속하여,
# 악성코드를 염두에 두어 정보를 온전히 주지 않는 경우가 있음

# >>> 비교용(정보가 깨지는 경우)
# import requests
# res = requests.get("http://nadocoding.tistory.com")
# res.raise_for_status()
# with open("nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)