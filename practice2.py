# 리스트 : 순서를 가지는 객체의 집합
subway = ["유재석",  "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.inser(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름ㅇ의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)

# 사전 -> '열쇠' : '사물함' 의 구조
cabinet = {3: "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5]) # 에러 발생

print(cabinet.get(3))
print(cabinet.get(100))
print(cabinet.get(5)) # 에러가 발생해도 `none` 처리가 됨

print(3 in cabinet)
print(5 in cabinet)

cabinet["3"] = "이정완"
cabinet["100"] = "alchemist_dev"

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())