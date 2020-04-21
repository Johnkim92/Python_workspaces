# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:37:06 2020

@author: USER
"""


import errno
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests, re, os

# 저장 폴더를 생성
try:
    if not (os.path.isdir('exercise_image')):
        os.makedirs(os.path.join('exercise_image'))
        print("image 폴더 생성 성공!")
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()
        
# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get('https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000003')
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

data1_list = soup.findAll('ul',{'class':'type_normal'})

li_list=[]

for data1 in data1_list:
    # 제목+썸네일 영역 추출
    li_list.extend(data1.findAll('li'))
    # 해당 부분을 찾아 li_list와 병합
    
for li in li_list:
    img = li.find('div',{'class':'thumb_area'}).find('img')
    title = img['alt']
    img_src = img['data-original']
    # 해당 영역의 글자가 아닌 것은 ''로 치환 시킨다.
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    # 주소, 파일경로+파일명+확장자
    urlretrieve(img_src, './exercise_image/'+title+'.jpg')
    
import sqlite3
import pandas as pd
con = sqlite3.connect("c:/acon_python/디지털가전.db")

price_list = []
name_list = []
for li in li_list:
    prices = li.find('div',{'class':'price'}).find('span',{'class':'num'}).text
    names = li.find('div',{'class':'thumb_area'}).find('img')['alt']
    prices =  int(re.sub('[^0-9]', '', prices))
    price_list.append(prices)
    name_list.append(names)

electronics = {'상품명':name_list, '가격':price_list}
    
electronics_top100 = pd.DataFrame(electronics, columns=['상품명','가격'])

electronics_top100.to_sql('elecAndDigits',con)
con.commit()

con.close()




    
    