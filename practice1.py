# -- 문자열 --  
# sentence = '나는 소년입니다.'
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)
# -- 문자열 --

# -- 슬라이싱 --
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0번째부터 2번째 미만까지의 값
# print("월 : " + jumin[2:4]) 
# print("일 : " + jumin[4:6])
# # print("생년월일 : " + jumin[0:6]) # 이것두 가능함
# print("생년월일 : " + jumin[:6]) # 처음부터 6 미만까지의 값
# # print("뒤 7자리 : " + jumin[7:14]) # 이것두 가능함
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝자리까지
# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])
# -- 슬라이싱 --

"""
# -- 문자열 처리 함수 --
python = "Python is Amazing"
print(python.lower()) # 소문자 출력
print(python.upper()) # 대문자 출력 
print(python[0].isupper()) # 첫번째 글자가 대문자야 ? 
print(len(python)) # 문자열의 총 길이를 구해줌
print(python.replace("Python", "Java")) # Python을 Java 로 바꿔줌

index = python.index("n") # n의 위치가 어디있는지 
print(index)

# 위의 index값을 기준으로 1을 더한 위치에서 부터 
# n의 위치를 찾음
index = python.index("n", index+1); 
print(index)

print(python.find("Java")) # 원하는 값이 없으면 -1 을 반환
# print(python.index("Java")) # 원하는 값이 없으면 에러를 뱉음
print(python.count("n")) # python이라는 문장안에서 n 이 몇번 나오는지 확인하는거임
# -- 문자열 처리 함수 --
"""

# -- 문자열 포맷 --
'''
# 방법 1
print('나는 %d살입니다.' %20) # d는 정수를 의미함
print("나는 %s을 좋아해요." %"파이썬") # s는 문자열을 의미함
print("Apple은 %c로 시작해요." %"A") # c는 Character를 의미함

# %s로 모두 통합가능
print('나는 %s살입니다.' %20) # d는 정수를 의미함
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강")) # 매개변수를 순서대로 입력
'''

'''
# 방법2
print("나는 {}살입니다.".format(20)) # format안에 있는 값을 중괄호에 넣음
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # format안에 있는 매개변수를 순서대로 전달
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # format안에 있는 매개변수를 순서대로 전달
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # format안에 있는 숫자로 순서 바꿀수도있음
'''

'''
# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간")) # 변수선언도 가능
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간" , age = 20 )) # 변수선언도 가능
'''

# 방법 4 (v3.6 이상 ~ )
'''
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
'''
# -- 문자열 포맷 --


'''
# -- 탈출 문자 --
# \n -> 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# \" \' 문장 내에서 따옴표
# 저는 "나도코딩" 입니다.
# print('저는 "나도코딩"입니다.')
print('저는 \"나도코딩\" 입니다.')
print('저는 \'나도코딩\' 입니다.')

# \\ -> 문장 내에서 \
print("/Users/wanni/Documents/python_lab/PythonWorkspace")

# \r -> 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b -> 백스페이스 역할(한글자 지우는거임)
print("Redd\bApple")

# \t -> 탭 역할
print("Red\tApple")
# -- 탈출 문자 --
'''

'''
# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

#(출력문 예제)
# 생성된 비밀번호 : nav51!

url = "http://google.com"
print(f"url의 값은 => {url}")
url = url.replace("http://", "")
print(f"http:// 제외, url의 값은 => {url}")
url = url[:url.index(".")]
print(f".com 제외, url의 값은 => {url}")
part1 = url[0:3]
print(f"part1의 값은 => {part1}")
part2 = len(url)
print(f"part2의 값은 => {part2}")
part3 = url.count("e")
print(f"part3의 값은 => {part3}")
part4 = "!"
print(f"생성된 비밀번호 : {part1}{part2}{part3}{part4}")
'''