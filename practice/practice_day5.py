# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(balance)

# 기본값
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", "20", "파이썬")
profile("김태호")

# 가변인자
def profile(name, age, *language):
    print("이름 : {0}, 나이 : {1}".format(name, age), end = " ")
    for lang in language:
        print(lang)

profile("유재석", "20", "파이썬", "자바")

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         *함수명 : std_weight
#         *전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(gender, height):
    if gender == "남자":
        return height ** 2 * 22
    else:
        return height ** 2 * 21

gender = "남자"
height = 175.5
weight = round(std_weight(gender, height / 100), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
