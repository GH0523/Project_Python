import re # Regular expression

p = re.compile("ca.e") # p 로 통용(pattern)
# . (ca.e)  : 하나의 문자를 의미 > caae, cabe, cace (O) | cadde (X)
# ^ (^de)   : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)   : 문자열의 끝 > case, base (O) | face (X)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열 그대로 출력
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 + 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("care") # match : 주어진 문자열의 처음부터 일치하는지 확인 > careless => care
# print_match(m)
# print(m.group()) # 매치되지 않을 시 에러 발생

# m = p.search("good care") # search : 주어진 문자열 중 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("care cave caffe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)



# 짚고 넘어가기

# 1. p = re.compile("원하는 형태")
# 2-1. m = p.match("비교할 문자열") : 주어진 문자열이 "완전히" 일치하는지 확인
# 2-2. m = p.search("비교할 문자열") : 주어진 문자열 "중에" 일치하는게 있는지 확인
# 2-3. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "list" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e)  : 하나의 문자를 의미 > caae, cabe, cace (O) | cadde (X)
# ^ (^de)   : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)   : 문자열의 끝 > case, base (O) | face (X)

# w3school > RegEx 관련 공부 가능
# python re > docs > "