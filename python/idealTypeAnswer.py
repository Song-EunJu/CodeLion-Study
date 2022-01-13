# dictionary 로만 관리 {'질문1':'답변1', '질문2':'답변2'}
total = {}
while True:
    question = input("질문을 입력해주세요 : ")
    if (question == 'q'):
        break
    total[question]=""

for question in total:
    print(question)
    answer = input(">> 답변을 입력해주세요 : ")
    total[question]=answer

print("결과 : ", total)

# list 안에 dictionary 객체로 관리 
# [
#     {'질문:'질문1', '답변':'답변1'}
#     {'질문:'질문1', '답변':'답변1'}
# ]

total=[]
while True:
    question = input("질문을 입력해주세요 : ")
    if (question == 'q'):
        break
    total.append({'질문':question, '답변':""})

for question in total:
    print(question['질문'])
    answer = input(">> 답변을 입력해주세요 : ")
    question['답변']=answer

print("결과 : ", total)