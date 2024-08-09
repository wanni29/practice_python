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

# 인덱스 번호로도 제거할수있음 
# 심지어 제거된 사람이 누구인지도 정확하게 나옴
print(subway.pop(0))

# remove 같은 경우는 복사가 안됨 
# 그래서 에러를 발생시키고 프로그램이 종료가 되어 버림
# 사용방법은 단순히 값만 제거하고 print로고로는 리스트를 찍어서 확인해야하는 
# 불편함이 있음
# 그래서 코드를 아래와 같이 구성해야함
# -> 차라리 pop쓰고 말지 !
subway.remove("유재석")
print(subway) 



# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 참 신기한 점은 복사와 원본이라는 개념임
# 계속해서 마주 하는 문제이자 에러인데 정확히 잡고 넘어가는게 좋을거 같음
# 지금 같은 경우는 원본에만 데이터가 변경이 되고 복사가 되지 않기 때문에 
# print 문으로 감싸서 볼수가 없음 -> 에러 터지고, 프로그램이 종료가 되어버림
print(num_list.sort()) # None 

# 그런데 특이한거는 sorted()로 감싸고 print()문으로 찍어보면 찍힘 
# 내가 보기엔 복사가 되는 거 같음
# 이렇게 원본과 복사에 대해서 접근해도 괜찮고
# 리턴값을 주냐 안주냐로 접근해도 괜찮음
# 무슨 말이냐면, sort()함수는 리턴값을 제공하지 않음 
# 그래서 변수에 담을수 없는거고, print 문에도 찍히지 않는거임
# 반면에, sorted() 함수는 리턴값을 제공함 
# 그래서 변수에 담을수 있는거고, print 문에도 찍히는 거임
print(sorted(num_list)) # [1, 2, 3, 4, 5]

sorted_list = sorted(num_list)
# reversed() 메소드는 리턴값을 이터러블 타입으로 주는데
# 그값은 리턴값이 리스트가 아니기 때문에 리스트로 다시 타입을 묶어주는거임 
reverse_sorted_list1 = list(reversed(sorted_list))
print(f"복사의 개념에서 reverse_sorted_list1의 값은 다음과 같습니다 : {reverse_sorted_list1}")
reverse_sorted_list2 = sorted_list.reverse()
print(f"원본의 개념에서 reverse_sorted_list2의 값은 다음과 같습니다: {reverse_sorted_list2}")

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

