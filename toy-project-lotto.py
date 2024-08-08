from random import *
import time

def typewriter_effect(text, delay=0.05):
    for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
    print() # 줄바꿈


starting = "--------------로또 번호 생성기--------------"

# 리스트를 저장할 딕셔너리
number_dict = {}
final_dict ={}

# 6개의 리스트를 만들고
# 딕셔너리에 담는다.
for i in range(1, 6):
    number_dict[f"number_section_list{i}"] = []

# 각 리스트에 랜던함 번호를 추가
for i in range(1, 6):
    while len(number_dict[f"number_section_list{i}"]) < 6:
        number = randint(1, 45)
        if number not in number_dict[f"number_section_list{i}"]:
            number_dict[f"number_section_list{i}"].append(number)

# 번호를 정렬
for i in range(1, 6):
        number_dict[f"number_section_list{i}"] = sorted(number_dict[f"number_section_list{i}"])

# 딕셔너리를 리스트로 변환하여 첫 번째 값 기준으로 정렬
sorted_lists = sorted(number_dict.values(), key=lambda x: x[0], reverse = False)


# 결과 확인 
typewriter_effect(starting)
for i, lst in enumerate(sorted_lists):
    message_number = f"{lst[0]}\t{lst[1]}\t{lst[2]}\t{lst[3]}\t{lst[4]}\t{lst[5]}"
    typewriter_effect(message_number)
ending = "--------------------------------------------"
typewriter_effect(ending)
