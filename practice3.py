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