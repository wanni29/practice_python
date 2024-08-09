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
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석",  age= 20, main_lang="파이썬")
profile(name = "유재석",   main_lang="파이썬", age= 20)
