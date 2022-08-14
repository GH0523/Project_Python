import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # 비정상 작동 시 오류 출력 후 종료
# print("응답코드 :", res.status_code) # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)



# 짚고 넘어가기
# .get > 원하는 url 정보 입력 가능