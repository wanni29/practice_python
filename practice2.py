'''
# -- 리스트 --
# 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가 ?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
# append를 하게 되면 리스트의 가장 맨 뒤에 추가가 된다.
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)
# -- 리스트 --
'''

'''
# -- 사전 --
# '열쇠 : 사물함' 의 구조
cabinet = {3: "유재석", 100 : "김태호"}

print(cabinet[3])
print(cabinet[100])


print(cabinet.get(3))
print(cabinet.get(100))

# -> 이렇게 했을경우에 
# -> 만약 키 값이 없는것을 찾게 되면 에러가 터져서 `프로그램 종료` 
print(cabine[5])

# -> 이렇게 했을 경우에
# -> 만약 키 값이 없는 것을 찾게 되면 에러가 터져도 `None` 이라고 표기
print(cabinet.get(5))
# -> 5라는 키값을 찾아오는데 없다면은 "사용 가능이라는 문구를 띄워라"라는 의미 
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False
cabinet = {"A-3" : "유재석" , "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# value 값들만 0으로 만들기
cabinet = cabinet.fromkeys(cabinet, 0)
print(cabinet)

# 목욕탕 폐점
# cabinet.clear()
# print(cabinet)
# -- 사전 --
'''

