import requests
from bs4 import BeautifulSoup as bs

NAVER_NEW_URL = "https://news.naver.com/main/ranking/popularDay.nhn"
response = requests.get(NAVER_NEW_URL)
data = response.text
soup = bs(data,'html.parser')
all_div = soup.find_all("ul",{"class":"section_list_ranking"})
URL = []
TITLE = []
for EACH_TAG in all_div:
    ALL_A_TAG = EACH_TAG.find_all("a")
    for i in ALL_A_TAG:
        if(i.has_attr('href')):
            URL.append(i.get('href'))
            TITLE.append(i.get("title"))
PATH = "https://news.naver.com/"
print(len(URL))
for i in range(len(URL)):
    if i < 10:
        print("정치) ",end="")
    elif i < 20:
        print("경제 ) ",end="")
    elif i < 30:
        print("사회 ) ",end="")
    elif i < 40:
        print("생활/문화 ) ",end="")
    elif i < 50:
        print("세계 ) ",end="")
    else:
        print("IT/과학 ) ",end="")
    print(TITLE[i])#PATH+URL[i])
