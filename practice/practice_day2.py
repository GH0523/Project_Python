# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

#문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
print(python.index("n"))
print(python.index("n",python.index("n") + 1))
print(python.find("Java"))
print(python.count("n"))

# 문자열포맷
# 방법1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요" % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
print("나는 {}을 좋아해요.".format("파이썬"))
print("나는 {}과 {}를 좋아해요".format("파이썬", "자바"))
print("나는 {1}와(과) {0}을(를) 좋아해요".format("파이썬", "자바"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
#\" \' : 문장 내 따옴표
print("저는 \"여규한\"입니다.")
# \\ : 문장 내 \
print("C:\\Users\\USER\\Desktop\\Python 3.9\\PythonWorkspace")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스
print("Redd\bApple")
# \t : 탭
print("Red\tApple")

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#예) http://naver.com
#규칙1 : http:// 부분은 제외 >>> naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외 >>> naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!' 로 구성
#예) 생성된 비밀번호 : nav51!

URL = "https://google.com" #링크 입력
process = URL.replace("https://","") #규칙1
process = process[:process.index(".")] #규칙2(슬라이싱, index 사용)
password = process[:3] + str(len(process)) + str(process.count("e")) + "!" #숫자값을 문자값과 더할때는 str 유념
print(f"\"{URL}\"의 비밀번호는 \"{password}\"입니다.")