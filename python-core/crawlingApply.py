import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://datalab.naver.com/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser') # response.test 를 html.parser를 이용해 의미있는 데이터 구성으로 만드는 것 

# response.test 값을 naverRank.html 에 옮기기 
file = open("./python-core/naverRank.html","w",encoding='UTF-8')
file.write(response.text)
file.close()

search_rank_file = open("./python-core/rankresult2.txt", "w", encoding='UTF-8') # file 열기

print("\n")
print(datetime.today().strftime("%Y년 %m월 %d일의 분야별 인기 검색어 순위입니다. \n"))

rank = 1
for i in soup.findAll('a', {'class':['title','list_area']}):
    # print(i)
    print((i.find('span').text))
    search_rank_file.write(str(rank)+"위:"+i.get_text()+"\n")
    print(rank,"위:",i.get_text()+"\n")
    rank+=1