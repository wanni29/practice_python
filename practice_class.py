# class Unit: 
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# # 다중 상속을 받을때에 super().__init__을 사용하게 되면 
# # 마지막에 있는 친구만 상속을 제대로 받기 때문에 
# # 다중 상속을 사용할것이라면, 차라리
# # Flyable.__init__(self, ...)
# # Unit.__init__(self, ...)
# # 이렇게 접근하는게 좋음

# # 이렇게 된다면 
# # 로그문 두가지가 같이뜸
# class FlyableUnit(Flyable , Unit):
#     def __init__(self):
#         Unit.__init__(self)
#         Flyable.__init__(self)

# # 드랍쉽
# dropship = FlyableUnit()

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [제공된 코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        # 멤버 변수
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    # 매물 정보 표시
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}", sep="")

apart = House("강남", "아파트", "매매", "10억", "2010년")
office = House("마포", "오피스텔", "전세", "5억", "2007년")
vila = House("송파", "빌라", "월세", "500/50", "2000년")

place_list = []

place_list.append(apart)
place_list.append(office)
place_list.append(vila)

print("총 3대의 매물이 있습니다.")
for place in place_list:
    place.show_detail()