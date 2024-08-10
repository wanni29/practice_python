# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# from travel import *
# import inspect
# import random
# # 패키지나 모듈의 위치 알아내기
# print(inspect.getfile(random)) 
# print(inspect.getfile(thailand))

# 내가 원하는 라이브러리 찾아보기 
# -> https://pypi.org/project/beautifulsoup4/
# -> 라이브러리 다운 명령어 복사 
# -> 명령어 입력 : pip install beautifulsoup4
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
# pip list -> 현재 설치되어있는 리스트 목록
# pip show beautifulsoup4 -> beautifulsoup4에 대한 정보를 알수있음
# pip install --upgrade beautifulsoup4 
# pip uninstall beautifulsoup4

# -- 내장 함수 --
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.".format(language))

# dir : 어떤 객체를 넘겨줬을 때  그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random)) # random 함수안에 어떠한 메소드나 객체가 있는지
# lst = [1, 2, 3]
# print(dir(lst))

# name = "SH"
# print(dir(name))

# Google 검색 : list of python builtins
# 파이썬에서 사용 할 수 있는 내장 함수 전체를 제공
# -- 내장 함수 --

# -- 외장 함수 --
# Google 검색 : list of python modules
# glob : 경로 내의 폴더  / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # -> 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 표시 

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는  폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘 부터 100일 후
# -- 외장 함수 --

# Quiz) 나만의 모듈과 파일을 이용하여 sign 로고문 출력하기
from sign import *
byme.sign()