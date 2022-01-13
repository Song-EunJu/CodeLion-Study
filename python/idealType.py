question_list = list()
while True:
    question = input("질문을 입력해주세요 : ")
    if (question == 'q'):
        break
    question_list.append(question)


print(question_list)
print("=======================================")

total={}

for question in question_list:
    print(question)
    answer = input(">> 답변을 입력해주세요 : ")
    total[question]=answer
    print("\n")

print("결과 : ", total)

