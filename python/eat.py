# 파이썬에서 기본으로 제공하지 않는 기능을 위해서는 import 가 필요
import time
import random

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("뭐 먹고 싶니 : ")
    if item == 'q':
        break
    else:
        lunch.append(item)

print(lunch)

set_lunch = set(lunch) # list -> set 변환
while True:
    print(set_lunch)
    item = input("뭘 먹기 싫니 : ")
    if item == 'q':
        break
    else:
        set_lunch = set_lunch - set([item])


print(set_lunch, "중에서 선택해라")

print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(random.choice(list(set_lunch))) # 랜덤으로 뽑기 위해 set -> list 로 변환