# if문

# 1. 기초 1번
'''
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")
'''

# 2. 기초 2번
'''
temp = int(input("기온은 어때요 ?"))
if  30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
'''

# for문

# 1. randrange()
for waiting_no in range(1,6):  # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{}님, 커피가 준비되었습니다.".format(customer))

# 2. while
customer = "스파이더맨"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분 되었습니다.")

# 3. 무한 루프
customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index += 1

# 4. 무한 루프2
customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}님, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요 ?")

# 5. Continue 와 Break [집중]
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡 했음
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지, {student}는 교무실로 따라와!")
        break
    print(f"{student}, 책을 읽어봐")

# 한줄 for문

# 1. 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]
print(students)

# 2. 학생 이름을 길이로 변환 
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 3. 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# 4. 학생 이름을 소문자로 변환 
students = ["Iron man", "Thor", "I am groot"]
students = [i.lower() for i in students]
print(students)

'''
# 퀴즈
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 :  승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ]  2번째 손님 (소요시간 : 50분)
# [0]  3번째 손님 (소요시간 : 5분)
# ...
# [] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 명 

from random import *

# 손님 50명 변수에 담기 
clients = range(1, 51)
clients = list(range(1, 51))

# 소요시간 정하기
past_times = list(range(5, 51))

# 난수로 정하기 -> sample 함수 사용
sample(past_times, 1)

# 필터링 조건
filters = list(range(5, 16))

print(filters)

# 최종 탑승 승객 인원 수
final_my_clients = 0

# 로직 구성 시작
for client in clients:
    setting_time = sample(past_times, 1)[0]
    if setting_time in filters:
        print(f"[O] {client}번째 손님 (소요시간 : {setting_time})")
        final_my_clients += 1
    else:
        print(f"[ ] {client}번째 손님 (소요시간 : {setting_time})")

# 최종 인원 출력 로고
print(f"총 탑승 승객: {final_my_clients} 명")
'''