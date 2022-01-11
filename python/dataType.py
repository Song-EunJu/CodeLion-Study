# dictionary
info = {"고향": "수원", "취미": "영화관람", "좋아하는 음식" : "국수", "특기":"피아노", "사는 곳":"서울"}
print(info)
print(info.get("고향"))
print(info.get("사는 곳"))

# list, dictionary
information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
foods = ["된장찌개", "피자", "제육볶음"]
information["특기"]="피아노" # dictionary 항목 추가
information["사는 곳"]="서울"
del information["좋아하는 음식"] # dictionary key 삭제
print(information) 
print(len(information))
information.clear() # dictionary 비우기
print(information)

print(foods[0])
print(foods[-1]) # 뒤에서부터 0번째 요소
foods.append("김밥")
print(foods)
del foods[3]
print(foods)