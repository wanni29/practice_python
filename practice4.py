# # 함수
# def open_account() :
#     print("새로운 계좌가 생성 되었습니다.")

# # 입금
# def deposit(balance, money): 
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# # 출금
# def withdraw(balance, money):
#     if balance >= money: #잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money 
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))

# # 야간 출금 - 수수료
# def withdraw_night(balance, money):
#     commission = 100 # 수수료 값
#     return commission, balance - money - commission


# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이: {1}\t주 사용 언어 : {2}"  \
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이: {1}\t주 사용 언어 : {2}"  \
#           .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석",  age= 20, main_lang="파이썬")
# profile(name = "유재석",   main_lang="파이썬", age= 20)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    # print("이름: {0}\t나이 : {1}\t".format(name, age), end= " ")
    # print(lang1, lang2, lang3, lang4, lang5)

# 가변 인자
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "Java", "C", "C++", "C#", "javascript")
# profile("김태호", 25, "kotlin", "swift")
# profile("이정완", 31, "javascript", "dart", "python",{1,2,3} )

# -- 지역 변수 --
#지역 변수(함수 안에서만 사용가능)와 전역 변수(어디서든 사용 가능)
# gun = 10

# def checkpoint(soldiers) : #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
# -- 지역 변수 --

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
#   남자 : 키 (m) x 키 (m) x 22
#   여자 : 키 (m) x 키 (m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산 
#               * 함수명 : std_weight
#               * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

import math

height = int(input("키를 입력하세요(예: 163) :"))
gender = input("성별을 입력하세요(예: 남/여) :")

def std_weight(height, gender) : 
    height = height/100
    if gender == "남" :
        return height * height * 22
    else : 
        return height * height * 21

result = std_weight(height, gender)
result = round(result, 2)
print(result)


print(f"키 {height} {gender}의 표준 체중은 {result}kg 입니다.")
    
