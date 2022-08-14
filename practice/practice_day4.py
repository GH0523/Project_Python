# if
weather = "미세먼지"
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
elif weather == "폭염" :
    print("양산을 챙기세요")
else :
    print("준비물이 없어요")

temp = int(input("기온은 어때요? "))
if 30 < temp:
    print("너무 더워요")
elif 10 <= temp <=30:
    print("날씨가 적당해요")
elif 0 <= temp and temp < 10:
    print("날씨가 추워요")
else :
    print("너무 추워요")

# for
for waiting_no in range(1, 5) :
    print("대기번호 : {}".format(waiting_no))

starbucks = ["a", "b", "c"]
for waiting_no in starbucks :
    print("{}, 주문하신 메뉴 나왔습니다.".format(waiting_no))

# while
customer = "a"
index = 5
while index >= 1 :
    print("{0}, 메뉴 나왔습니다. {1}번 잔여.".format(customer, index))
    index -= 1
    if index == 0:
        print("메뉴는 폐기처분 되었습니다.")

# continue 와 break
absent = [2, 4] # 결석 학생
no_book = [6]   # 책을 까먹은 학생
for student in range(1, 8):
    if student in absent:
        continue
    elif student in no_book:
        print("금일 수업 종료. {0}번 학생, 교무실로.".format(no_book))
        break
    else :
        print("{0}번 학생, 책 읽어보세요.".format(student))

# 한 줄 for
students = [1, 2, 3, 4, 5]
students = [a + 100 for a in students]
print(students)

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

# for
from random import *
cnt = 0
for i in range(1, 51):
    time = randint(5, 50)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print(f"총 탑승 승객 : {cnt} 분")

# while
from random import *
cnt = 0
index = 1
while index <= 50:
    time = randint(5, 50)
    if 5 <= time <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(index, time))
        cnt += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(index, time))
    index += 1
print(f"총 탑승 승객 : {cnt} 분")