from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup as bs

#name = "이지호" #이름
#birth = "1999-02-06" #생년월일
#duty = "2020-01-13" #입대일
#training = TRAINING_LIST.index("육군훈련소(27연대)")#입영부대


class MAIN:
    TRAINING_LIST = [0, '1', '1사단','2사단', '3사단', '5사단', '6사단', '7사단',
    '9사단', '11사단', '12사단', '15사단', '17사단', '20사단', '21사단', '22사단',
    '23사단', '25사단', '27사단', '28사단', '30사단', '31사단', '32사단', '35사단',
    '36사단', '37사단', '39사단', '50사단', '51사단', '53사단', '55사단', '육군훈련소',
    '육군훈련소(23연대)', '육군훈련소(25연대)', '육군훈련소(26연대)', '육군훈련소(27연대)',
    '육군훈련소(28연대)', '육군훈련소(29연대)', '육군훈련소(30연대)']
    #변수 선언부
    kakao_ID = "" #카카오톡 ID
    kakao_PW =  ""        #카카오톡 비밀번호
    driver = webdriver.Chrome('chromedriver')

    def __init__(self,kakao_ID,kakao_PW):
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.thecamp.or.kr/eduUnitCafe/viewEduUnitCafeMain.do") #메인화면 접속
        self.kakao_ID = kakao_ID
        self.kakao_PW = kakao_PW
        self.kakaoLogin()


    def kakaoLogin(self):
        self.driver.find_element_by_xpath('''//*[@id="mainForm"]/div/section/div[5]/a[1]''').click()
        self.driver.find_element_by_xpath('''//*[@id="id_email_2"]''').send_keys(self.kakao_ID)
        self.driver.find_element_by_xpath('''//*[@id="id_password_3"]''').send_keys(self.kakao_PW)
        self.driver.find_element_by_xpath('''//*[@id="login-form"]/fieldset/div[8]/button''').click()
        time.sleep(1)


    def registerSoldier(self,name,birth,duty):
        self.driver.get("https://www.thecamp.or.kr/missSoldier/viewMissSoldierSearch.do")
        self.driver.find_element_by_xpath("""//*[@id="missSoldierClassCd"]/option[2]""").click() #성분 선택
        self.driver.find_element_by_xpath("""//*[@id="grpCd"]/option[2]""").click() #육군 선택 2육군 3해군 4공군 5해병대 6국방부
        self.driver.find_element_by_xpath("""//*[@id="name"]""").send_keys(name) #이름 설정
        self.driver.find_element_by_xpath("""//*[@id="birth"]""").send_keys(birth) #생년월일
        self.driver.find_element_by_xpath("""//*[@id="enterDate"]""").send_keys(duty) #입영일
        self.driver.find_element_by_xpath("""//*[@id="trainUnitCd"]/option[{}]""".format(training)).click() #입영부대
        self.driver.find_element_by_xpath("""//*[@id="missSoldierRelationshipCd"]/option[8]""").click()
        self.driver.find_element_by_xpath("""//*[@id="searchBtn"]""").click()
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        self.driver.get("https://www.thecamp.or.kr/eduUnitCafe/viewEduUnitCafeMain.do")


    def getNews(self):
        PATH = "https://news.naver.com/"
        NAVER_NEWS_URL = "https://news.naver.com/main/ranking/popularDay.nhn"
        response = requests.get(NAVER_NEWS_URL)
        data = response.text
        soup = bs(data,'html.parser')
        all_div = soup.find_all("ul",{"class":"section_list_ranking"}) #div 태그의 class 가 section_list_ranking 을 찾음
        URL = []
        TITLE = []
        for EACH_TAG in all_div:
            ALL_A_TAG = EACH_TAG.find_all("a") #모든 a 태그를 찾음
            for i in ALL_A_TAG: #a 태그에서 href 옵션이 있으면
                if(i.has_attr('href')):
                    URL.append(i.get('href')) #해당 url 과
                    TITLE.append(i.get("title")) #title 을 저장

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



ID = ""
PW = ""
a = MAIN(ID,PW)
