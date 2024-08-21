# [정리] 
# -- 표준 입출력 --
# sep, default 값 : sep = " "
# end, default 값 : end = "\n"
print("Python", "Java", "Javascript", sep=" vs ", end=' Winner : Python')

# -- 좌, 우 정렬 -- 
# 리스트.items() : 키, 밸류값
# string.ljust(8) : 왼쪽 정렬을 하고 글자 포함 8칸
# string.rjust(4) : 오른쪽 정렬을 하고 글자 포함 4칸
string = "이정완"
print(string.ljust(8))
print(string.rjust(8))
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# -- zfill(3) -- 
# 은행 대기 순번표
# 001, 002, 003, ...
# String.zfill(3) => 3자리수를 나타낼것인데 3개의 공간에 
# 수가 들어가지 않는 부분에서 0을 채우자!
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# -- input으로 값을 받으면 String --
# input으로 입력받는 값은 String 값으로 받게되기 때문에
# 숫자형 문자열이라면 
# int() / float() 라는 값으로 감싸줘야한다.

# -- 다양한 출력 포맷 --
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))
# 양수일 땐 `+` 로 표시, 음수일 땐 `-`로 표시
print("{0: >+10}".format(-500))
print("{0: >+10}".format(+500))
# 왼쪽 정렬하고, 빈칸으로 `_`으로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리마다 콤마 찍어주기 , +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))
# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
print("{0:^<+30,}".format(10000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))


# -- 파일에 내용을 적고 저장하기 및 읽어오기 -- 
# 파일을 열되, 한글이 포맷이 가능한 "utf8"로 연다
score_file = open("score.txt", "w", encoding="utf8")
# print는 여기서 `기록하는` 용도로 쓰임
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
# 파일을 열었으면 닫는것까지 해주어야 한다.
score_file.close() 

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("수학 : 0\n")
score_file.write("영어 : 50\n")
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100")
score_file.close() 

score_file = open("score.txt" , "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

# 파일 입출력은 open하구, close로 또 닫아야 하기 때문에
# with코드로 끝내버리자
# with :  파일을 열고 닫는 작업을 조금 더 수월하게 만들 수 있도록 도와줌
import pickle
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

'''
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
'''