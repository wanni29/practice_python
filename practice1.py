# practice1 소스코드 및 개념 정리

# 간단하게 변수에 문자열을 담을 수 있다.
sentence = "나는 소년입니다."
print(sentence)

# 긴 문자열은 이런식으로 담을 수 있다.
long_sentence = '''
나는 소년이고,
파이썬은 쉬워요.
'''
print(long_sentence)

# 슬라이싱에 관하여
jumin = "990120-1234567"
print("성별 : " + jumin[7]) # 인덱스 7번째 자리
print("연 : " + jumin[0:2]) # 인덱스 2번째 미만 까지의 값
print("월 : " + jumin[2:4]) 
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])

# 문자열 처리에 관한 함수 
python = "Python is Amazing"
print(python.lower()) # 소문자로  
print(python.upper()) # 대문자로
print(python[0].isupper()) # 0번째 인덱스가 대문자야?
print(len(python)) # 길이 구하기
print(python.replace("Python", "Dart")) # 대처하기

#n의 위치가 어디야?
index = python.index("n") 
print(index)
# index의 위치에서 +1 한 인덱스 부터 시작해서 n이 있는곳을 찾아줘!
next_index = python.index("n", index+1) 
print(next_index)
# 원하는 값이 없으면 -1을 반환
print(python.find("Java"))
# 원하는 값이 없으면 에러를 뱉음(프로그램 종료)
print(python.index("Java"))
# python이라는 문장 안에서 n이 몇번 나오는지 확인 
print(python.coun("n"))

# 문자열 포맷에 관하여
print("나는 %d살입니다."  %20)
print("나는 %s을 좋아해요." %"파이썬")
print("Apple은 %c로 시작해요." %"A")

# %s로 통합가능
print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color= "빨간"))
print("나는 {age}살이먀, {color}색을 좋아해요.".format(color="파란", age=31))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
# \n : 줄바꿈
# \" : 문장 내에서 따옴표
# \\ : 문장 내에서 \
# \r : 커서를 맨 앞으로 이동
# \b : 백스페이스 역할
# \t : 탭 역할