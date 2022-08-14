# 정규식(Regular Expression) = (정해진 형태를 의미하는 식 {Ex) 주민등록 형식})


import re
p = re.compile("ca.e") # p : pattern
# . (ca.e) : 하나의 문자를 의미 > care, case, cave | caffe
# ^ (^de) : 문자열의 시작 > desk, destination | fade
# $ (se$) : 문자열의 끝 > case, base | set

m = p.match("careless") # match : 주어진 문자열의 "처음부터" 일치하는지 확인

# 매치 방법 - 1
print(m.group()) # 매치되지 않을 경우 에러 발생

# 매치 방법 - 2
if m:
    print(m.group())
else:
    print("Did not matched")

# 매치 방법 - 3
def print_match(m):
    if m:
        print("m.group():", m.group()) # group() : 일치하는 문자열 반환
        print("m.string:", m.string) # string : 입력받은 문자열 출력
        print("m.start():", m.start()) # start() : 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # end() : 일치하는 문자열의 끝 index
        print("m.span()", m.span()) # span() : 일치하는 문자열의 시작 / 끝 index
    else:
        print("Did not matched")

print_match(m)

m = p.search("good careless") # search : 주어진 문자열 "중에" 일치하는게 있는지 확인
print_match(m)

lst = p.findall("good care case, carre") # findall : 일치하는 모든 것을 리스트 형태로 반환 (이전까지는 맨 처음 발견되는 하나만 값에 대해 처리)
print(lst)


# 정리
# 1. p = re.compile("원하는 형태") [보통 p 라는 형태로 받아옴]
# 2. m = p.match("비교할 문자열") [위에서 받은 p 가 match 되는지 비교][주어진 문자열의 "처음부터" 일치하는지 확인]
# 3. m = p.search("비교할 문자열") [위에서 받은 p 가 match 되는지 비교][주어진 문자열 "중에" 일치하는게 있는지 확인]
# 4. lst = p.findall("비교할 문자열") [일치하는 모든 것을 list 형태로 반환]

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, case, cave | caffe
# ^ (^de) : 문자열의 시작 > desk, destination | fade
# $ (se$) : 문자열의 끝 > case, base | set