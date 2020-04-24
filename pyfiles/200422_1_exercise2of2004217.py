# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:12:19 2020

@author: USER
"""


import sqlite3
import pandas as pd
import numpy as np

con = sqlite3.connect('../20200421_김성겸/디지털가전.db') #db 파일 경로 넣기
read_df = pd.read_sql("select * from elecAndDigits", con) # 테이블 명 주의
con.close()
print(read_df['가격']) # 컬럼명 주의
mean_df = np.mean(read_df['가격']) # read_df.가격.mean()
max_df = np.max(read_df['가격'])
min_df = np.min(read_df['가격'])
first_df = np.percentile((read_df['가격']), 25) 
third_df = np.percentile((read_df['가격']), 75)
second_df = np.percentile((read_df['가격']), 50)
fourth_df = np.percentile((read_df['가격']), 100)
print('평균값 : ',mean_df,'\n 최댓값: ',max_df,'\n 최솟값: ',min_df,
      '\n 1분위 값: ',first_df, '\n 2분위값: ', second_df,
      '\n 3분위 값: ',third_df, '\n 4분위값: ', fourth_df)
import matplotlib.pyplot as plt
plt.figure()
plottingline= plt.plot(read_df.상품명, read_df.가격, color='coral', makrer='o', linestyle='---') # 객체명.컬럼명 = 객체명['컬럼명']
plt.xticks(rotation = 90, fontsize= 3)

plt.show()
