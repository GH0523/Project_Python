print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋ"*9)
# 참 / 거짓
print(5>10)
print(5<10)
print(not True)
print(not(5>10))
# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby="공놀이"
#print(name +  "는 " +str(age)+ "살이며, " + hobby + "을 아주 좋아해요")
print(name,  "는 " ,age, "살이며, " ,hobby, "을 아주 좋아해요")
print(name +"는 어른일까요?" + str(is_adult))

#Quiz) 변수를 이용하여 문장 출력하기
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

print(2**3) #2^3 = 8
print(5%3) #나머지 구하기 (=2)
print(5//3) #몫 구하지 (=1)
print(3+4 == 7) #앞뒤 값의 동일 여부 (True)
print(1 != 3) #앞뒤 값의 상이 여부 (True)

number = 2+3*4
print(number)
number = number + 2
print(number)
number+=2
print(number)

print(abs(-5)) #5 (절대값)
print(pow(4,2)) #4^2 = 16 (제곱)
print(max(5,12)) #12 (최대값)
print(min(5,12)) #5 (최소값)
print(round(3.99)) #4 (반올림)

# 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값
print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값

# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# 출력문 예제 : 오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.

date = int(random()*31)+4
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ",str(date),"일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 ",str(day),"일로 선정되었습니다.")