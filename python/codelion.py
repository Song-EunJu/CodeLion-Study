import random
import time

## 반복문
# while True:
#     print(random.choice(["된장찌개","치킨","떡볶이","라면","감자튀김"]))
#     print("이 문장도 반복되나")
#     break
#     time.sleep(1) 

## 변수 만들기
# lunch = random.choice(["된장찌개","피자","제육볶음"])
# dinner = random.choice(["김밥","쫄면","돈까스"])
# print(lunch, dinner)

## dictionary
# info = {"고향": "수원", "취미": "영화관람", "좋아하는 음식" : "국수", "특기":"피아노", "사는 곳":"서울"}
# print(info)
# print(info.get("고향"))
# print(info.get("사는 곳"))

## list, dictionary
# information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
# foods = ["된장찌개", "피자", "제육볶음"]
# information["특기"]="피아노" # dictionary 항목 추가
# information["사는 곳"]="서울"
# del information["좋아하는 음식"] # dictionary key 삭제
# print(information) 
# print(len(information))
# information.clear() # dictionary 비우기
# print(information)

# print(foods[0])
# print(foods[-1]) # 뒤에서부터 0번째 요소
# foods.append("김밥")
# print(foods)
# del foods[3]
# print(foods)

## 끝까지 반복하기
# for x in range(30):
#     print(x)

# foods = ["된장찌개", "피자", "제육볶음"]
# for x in foods:
#     print(x)

# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# for x,y in information.items():
#     print(x,y)

## 집합 (list와 다른 점은 순서가 없다는 것)
