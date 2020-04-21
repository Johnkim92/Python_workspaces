# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:54:28 2020

@author: USER
"""


# 네이버 웹툰 썸네일 가져오기

# 제목과 썸네일이 같이 존재하는 영역
from bs4 import BeautifulSoup
import requests

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 요일별 웹툰 영역 추출하기
data1 = soup.find('div',{'class':'list_area daily_all'})
data1 = data1.findAll('div',{'class':'col_inner'})
print(len(data1))

# 전체 웹툰 리스트
'''
요일별 웹툰 영역중 제목과 썸네일 영역을 하나의 리스트로
'''
list1=[]
for datas in data1:
    # 제목+ 썸네일 영역 추출
    # 해당 부분을 찾아 list1과 병합
    list1.extend(datas.findAll('li'))
    
print(len(list1))

# 각각의 요소중 <img> 태그의 제목과 썸네일(~.jpg)만 추출하기
for li in list1:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    print(title,img_src)
    

