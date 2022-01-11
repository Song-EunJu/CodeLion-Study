## 집합 Set _ list와 다른 점은 순서를 보장하지 않는다
# foods = ["된장찌개", "피자", "제육볶음"]
# foods_set1 = set(foods) # list를 set으로 변환
# foods_set2 = set(["된장찌개", "피자", "제육볶음"]) 
# print(foods_set1)
# print(foods_set2)

# 중복제거
# foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
# foods_set = set(foods)
# print(foods)
# print(foods_set)

# # 합집합
# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 | menu2
# print(menu3)

# # 교집합
# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 & menu2
# print(menu3)

# # 차집합 ( 겹친 메뉴인 된장찌개를 제외한 요소만 출력 )
# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 - menu2
# print(menu3)

## 문자열 -> set 으로 변환하기 _ 문자열 item -> 리스트 [item] -> 집합 set([item])
set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"

set_lunch = set_lunch - set([item]) 