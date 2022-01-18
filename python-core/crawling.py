import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.naver.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') # response.test 를 html.parser를 이용해 의미있는 데이터 구성으로 만드는 것 

file = open("./python-core/naver.html","w",encoding='UTF-8')
file.write(response.text)
file.close()

# print(soup.title) # <title>NAVER</title>
# print(soup.title.string) # NAVER
# print(soup.span) # span 태그 첫번째 요소만 가져오기
# print(soup.findAll('span')) # 모든 span 태그를 가져오기
# print(soup.findAll('a', 'issue')) # a 태그 중 issue class 가져오기

news_rank_file = open("./python-core/rankresult.txt", "a", encoding='UTF-8') # file 열기

print("\n")
print(datetime.today().strftime("%Y년 %m월 %d일의 인기 뉴스 순위입니다. \n"))

rank = 1
for i in soup.findAll('a', 'issue'):
    news_rank_file.write(str(rank)+"위:"+i.get_text()+"\n")
    print(rank,"위:",i.get_text()+"\n")
    rank+=1