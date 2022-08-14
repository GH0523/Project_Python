# requests = html 정보를 가져올 수 있도록 도움을 줌
# requests.get("링크 정보")

import requests
# res = requests.get("http://naver.com")
res = requests.get("http://nadocoding.tistory.com")
print("응답코드 :", res.status_code) # 웹페이지가 정상 상태인지 확인, 200 > 정상

# 오류 발생 여부 확인 - 1
if res.status_code == requests.codes.ok: #(=) == 200
    print("정상입니다")
else:
    print("문제 발생. [에러코드 :", res.status_code, "]")

# 오류 발생 여부 확인 - 2
res.raise_for_status() # 오류 발생 할 경우 바로 종료
print("웹 스크래핑을 진행합니다")

# 결국 통상적 방법은
# import requests
# res = requests.get("http://naver.com")
# res.raise_for_status()

print(len(res.text))
print(res.text)

with open("nado.html", "w", encoding="utf8") as f:
    f.write(res.text)