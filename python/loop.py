import random
import time

## 반복문
while True:
    print(random.choice(["된장찌개","치킨","떡볶이","라면","감자튀김"]))
    print("이 문장도 반복되나")
    break
    time.sleep(1) 

## 끝까지 반복하기
for x in range(30):
    print(x)

foods = ["된장찌개", "피자", "제육볶음"]
for x in foods:
    print(x)

information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
for x,y in information.items():
    print(x,y)

