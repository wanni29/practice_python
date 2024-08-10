# 표준 입출력
# print("Python", "Java", "Javascript", sep=" vs ", end=" => winner : Python") # Python vs Java vs Javascript

# 이거는 필수 개념인거 같음. 잘 알고 있자 !
# 문장의 끝부분을 `?` 로 바꿔 달라.
# 기본 디폴트 값으로 `\n`  이렇게 구성되어있었음
# print("Python", "Java", sep="," , end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# # 표준 출력으로 로고문이 찍힘
# print("Python", "Java", file=sys.stdout)
# # 에러 문으로 로고문이 찍힘
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# 리스트.items() => 키, 밸류값으로 나오게 됨!
# String.ljust(8) => 왼쪽 정렬을 하고 글자 포함 8칸
# String.rjust(4) => 오른쪽 정렬을 하고 글자 포함 4칸
# scores = {"수학" : 0, "영어" : 50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기 순번표
# 001, 002, 003, ...
# String.zfill(3) => 3자리수를 나타낼것인데 3개의 공간에 수가 들어가지 않은 
# 부분에서 0을 채워 달라
# for num in range(1, 21): 
    # print("대기번호 : " + str(num).zfill(3))

# 입력으로 값을 받게 되면 String 값으로 받게 된다.
# 숫자를 입력해도 String, 문자열을 입력해도 String으로 받게 됨
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# =================== 정리하기 ======================
'''
# 필수 개념 
print( ) 문안에는 `sep` 값과 `end`값이 포함되어있음
다만 디폴트 값으로 들어갔기때문에 따로 표기가 안되어있는거임
디폴트 값을 표기하자면 sep= " " / end = "\n"

file=sys.stdout() -> 표준 출력
file=sys.stderr() -> 에러 출력

리스트.items() -> 키, 밸류값으로 나오게 됨!
사용은 이런식으루 ->  for subject, score in scores.items():
String.ljust(8) -> 왼쪽 정렬을 하고 글자 포함 8칸
String.rjust(4) -> 오른쪽 정렬을 하고 글자 포함 4칸
String.zfill(3) -> 3자리수를 나타낼것인데 3개의 공간에 수가 들어가지 않은 
부분에서 0을 채워 달라

입력으로 값을 받게 되면 String 값으로 받게 된다.
'''
# =================== 정리하기 ======================

'''
# -- 다양한 출력 포맷 --
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))
# 양수일 땐 + 로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(-500))
print("{0: >+10}".format(+500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자릿수 까지만 표시 ( 소수점 3째 자리에서 반올림 )
print("{0:.2f}".format(5/3))
# -- 다양한 출력 포맷 --
'''

# -- 파일 입출력 --  
# score_file = open("score.txt", "w", encoding="utf8") # 파일을 열되, 한글이 포맷이 가능한 "utf8"로 연다.
# print("수학 : 0", file=score_file) # 여기서 print는 `기록한다`라는 의미인거 같음
# print("영어 : 50", file=score_file)
# score_file.close() # 파일을 열었으면 필수적으로 닫는것 까지 해주어야 함

# 여기서는 줄바꿈이 없기때문에 `\n` 직접 넣어줘야 함!
# score_file =open("score.txt", "a", encoding="utf8")
# score_file.write("수학 : 0")
# score_file.write("\n영어 : 50")
# score_file.write("\n과학 : 80")
# score_file.write("\n코딩 : 100") 
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="" )
# print(score_file.readline(), end="" )
# print(score_file.readline(), end="" )
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()
# -- 파일 입출력 --  

# -- Pickle --
# Pickle -> `프로그래밍 안의 데이터를 파일에 저장하는 행위`를 말함
# import pickle
# 여기서 `wb` 라는 것은 `write` + 'binary' 라는 의미임
# `binary` : 컴퓨터가 인식하는 0과 1로 이루어져 있음
# profile_file = open("profile.pickle", "wb") 
# profile = {"이름" : "박명수", "나이" : 31, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()
# -- Pickle --

# -- with --
# # with : 파일을 열고 닫는 작업을 조금더 수월하게 만들수있도록 도와줌 
# import pickle
# # 자동으로 자원관리를 함 -> profile_file.close()이라는 로직을 입력할 필요가 없음 
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
# -- with --

#  Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 - 
# 부서 : 
# 이름 : 
# 업무 요약 :

# 1주차 부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt' , ... 와 같이 만듭니다. 

import os
# 폴더 이름 지정
folder_name = "weekly_report"

# 폴더 생성
os.makedirs(folder_name, exist_ok=True)

# 1주차 ~ 50주차
weekly = list(range(1,51)) 

for week in weekly: 
    # 파일 경로를 폴더 안에 위치시키기
    file_path = os.path.join(folder_name, f"{week}주차.txt")

    with open(file_path, "w", encoding="utf8") as week_report:
        week_report.write(f" - {week}주차 주간보고 - ")
        week_report.write("\n부서:")
        week_report.write("\n이름:")
        week_report.write("\n업무 요약:")