from selenium import webdriver
import time


TRAINING_LIST = [0, '1', '1사단', '2사단', '3사단', '5사단', '6사단', '7사단', '9사단', '11사단', '12사단', '15사단', '17사단', '20사단', '21사단', '22사단', '23사단', '25사단', '27사단', '28사단', '30사단', '31사단', '32사단', '35사단', '36사단', '37사단', '39사단', '50사단', '51사단', '53사단', '55사단', '육군훈련소', '육군훈련소(23연대)', '육군훈련소(25연대)', '육군훈련소(26연대)', '육군훈련소(27연대)', '육군훈련소(28연대)', '육군훈련소(29연대)', '육군훈련소(30연대)']


#변수 선언부
kakao_ID = "" #카카오톡 ID
kakao_PW =  ""        #카카오톡 비밀번호


name = "이지호" #이름
birth = "1999-02-06" #생년월일
duty = "2020-01-13" #입대일
training = TRAINING_LIST.index("육군훈련소(27연대)")#입영부대


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.thecamp.or.kr/eduUnitCafe/viewEduUnitCafeMain.do") #메인화면 접속

#<-- 카카오톡 로그인부 시작 -->
driver.find_element_by_xpath('''//*[@id="mainForm"]/div/section/div[5]/a[1]''').click()
driver.find_element_by_xpath('''//*[@id="id_email_2"]''').send_keys(kakao_ID)
driver.find_element_by_xpath('''//*[@id="id_password_3"]''').send_keys(kakao_PW)
driver.find_element_by_xpath('''//*[@id="login-form"]/fieldset/div[8]/button''').click()
time.sleep(1)
#<-- 카카오톡 로그인부 끝-->

driver.get("https://www.thecamp.or.kr/eduUnitCafe/viewEduUnitCafeMain.do") #등록된 훈련병으로 이동


#등록하는거 만들어보기

driver.get("https://www.thecamp.or.kr/missSoldier/viewMissSoldierSearch.do")
driver.find_element_by_xpath("""//*[@id="missSoldierClassCd"]/option[2]""").click() #성분 선택
driver.find_element_by_xpath("""//*[@id="grpCd"]/option[2]""").click() #육군 선택 2육군 3해군 4공군 5해병대 6국방부
driver.find_element_by_xpath("""//*[@id="name"]""").send_keys(name) #이름 설정
driver.find_element_by_xpath("""//*[@id="birth"]""").send_keys(birth) #생년월일
driver.find_element_by_xpath("""//*[@id="enterDate"]""").send_keys(duty) #입영일
driver.find_element_by_xpath("""//*[@id="trainUnitCd"]/option[{}]""".format(training)).click() #입영부대


driver.find_element_by_xpath("""//*[@id="missSoldierRelationshipCd"]/option[8]""").click()
driver.find_element_by_xpath("""//*[@id="searchBtn"]""").click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
driver.get("https://www.thecamp.or.kr/eduUnitCafe/viewEduUnitCafeMain.do")
