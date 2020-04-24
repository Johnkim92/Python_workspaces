# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:16:58 2020

@author: USER
"""

# word cloud 설치
# 필요한 패키지들
'''
JDK 설치 : Java JDK로 검색해서 OS에 맞춰 설치
JAVA_HOME 설정 : 
JPype1 : conda install -c conda-forge jpype1
gensim install : pip install gensim
KoNLPy : pip install konlpy
WordCloud 설치 : pip install wordcloud
'''
'''
서울시 구별 CCTV 현황 분석하기

서울시 각 구별 CCTV 비율을 파악해서 순위 비교
인구대비 CCTV 비율을 파악해서 순위 비교
인구대비 CCTV의 평균치를 확인하고
그로부터 CCTV가 과하가ㅔ 부족한 구를 확인

Python 기본 문법 / Pandas와 Matplotlib의 기본적 사용법을 이용한 시각화
단순한 그래프 표현에서 한 단계 더 나아가 경향을 확인하고 시각화하는 기초확인
'''
import pandas as pd
import numpy as np

# CCTV 데이터와 인구 데이터 합치고 분석하기

# CCTV 데이터 읽기
CCTV_Seoul = pd.read_csv('../datas_and_pics/datas/01. CCTV_in_Seoul.csv', encoding='utf-8')
CCTV_Seoul.head()
CCTV_Seoul.columns
CCTV_Seoul.columns[0]

# 컬럼명 변경 : 기관명을 구별로 변경
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:'구별'}, inplace=True)
CCTV_Seoul.head()

# 인구 데이터 읽기1
pop_Seoul = pd.read_excel('../datas_and_pics/datas/01. population_in_Seoul.xls', encoding='utf-8')
pop_Seoul.head()

# 인구 데이터 읽기 2 - 필요한 데이터만 선별하여 읽기
pop_Seoul = pd.read_excel('../datas_and_pics/datas/01. population_in_Seoul.xls',
                          header = 2,
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8')
pop_Seoul.head()

# 알기 쉬운 컬럼 명으로 변경
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                          pop_Seoul.columns[1] : '인구수',
                          pop_Seoul.columns[2] : '한국인',
                          pop_Seoul.columns[3] : '외국인',
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)

# CCTV 데이터 파악하기
CCTV_Seoul.sort_values(by='소계', ascending=True).head(5)

CCTV_Seoul.sort_values(by='소계', ascending=False).head(5)

# 최근 증가율 = (2016년 + 2015년 + 2014년)/2013년도 이전*100
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] \
                       +CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] * 100

CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)

# 서울시 인구 데이터 첫 번째 합계행 삭제
pop_Seoul.drop([0], inplace=True)
# 구별 칼럼의 중복값 제거
pop_Seoul['구별'].unique()
# 구별 칼럼의 NULL 값 확인
pop_Seoul[pop_Seoul['구별'].isnull()]
# 구별 칼럼의NULL 값 있는 행 제거
pop_Seoul.drop([26], inplace=True)
pop_Seoul.head()

# 외국인 비율과 고령자 비율 추가
pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100
pop_Seoul.head()

# 각 컬럼 확인
pop_Seoul.sort_values(by='인구수', ascending=False).head(5)
pop_Seoul.sort_values(by='외국인', ascending=False).head(5)
pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5)
pop_Seoul.sort_values(by='고령자', ascending=False).head(5)
pop_Seoul.sort_values(by='고령자비율', ascending=False).head(5)

### CCTV 데이터와 인구 데이터 합치고 분석하기

# 두 개의 데이터 프레임을 합할 경우 동일 컬럼명은 하나('구별')로 통일된다.
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
data_result.head()

# CCTV에 대한 '소계'칼럼을 제외한 나머지 CCTV 데이터 삭제
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()

# 시각화 작업을 위한 구이름('구별')을 index화
data_result.set_index('구별', inplace=True)
data_result.head()

# CCTV와 각 칼럼에 대한 상관관계 분석
# 상관관계 함수 : np.corrcoef()
np.corrcoef(data_result['고령자비율'], data_result['소계'])
np.corrcoef(data_result['외국인비율'], data_result['소계'])
np.corrcoef(data_result['인구수'], data_result['소계'])
data_result.sort_values(by='소계',ascending=False).head(5)

data_result.to_csv('../datas_and_pics/datas/data_result.csv')

# CCTV와 인구현황 그래프로 분석하기
import platform

# 폰트 설정 (한글부분 특히)
from matplotlib import font_manager, rc
from matplotlib import pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system ... srry!')

# CCTV 비율을 구하고 그에 따른 시각화 작업
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100

data_result['CCTV비율'].sort_values().plot(kind='barh',grid=True, figsize=(10,10))
plt.show()

# 산점도 (인구수와 소계)
plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# 인구수와 CCTV는 상관 계수가 양의 값이므로 산점도와 직선
# 직선 구하기 (Polyfit을 이용한 회귀선)
# Polyfit 함수를 이용해서 예측 모델 Z의 계수를 생성
fp1 = np.polyfit(data_result['인구수'], data_result['소계'],1)
fp1

# 만들어진 예측 모델을 이용한 그래프 그리기
f1 = np.poly1d(fp1) # y축 데이터
fx = np.linspace(100000, 700000, 100) # x 축 데이터

plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx,f1(fx), ls='dashed', lw=3,color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# 회귀선을 통해 인구수가 3만명정도 일때 cctv의 수가 1100대 정도임을 알수 있다.
# 따라서 회귀선에 가까울수록 값이 적당하다 할 수 있다.

# 조금 더 설득력 있는 자료 만들기
'''
직선이 전체 데이터의 대표값 역할을 한다면
인구수가 3만일 경우 CCTV는 1100대 정도 여야 한다는 결론

가독성 향상을 위해 오차를 계산할 수 있는 코드 작성후,
오차가 큰 순으로 데이터를 정렬
'''
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
f1 = np.poly1d(fp1) # y축 데이터
fx = np.linspace(100000, 700000, 100) # x 축 데이터

data_result['오차']=np.abs(data_result['소계']-f1(data_result['인구수']))

df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort.head()

# plot 크기 설정
plt.figure(figsize=(14,10))

# 산점도
plt.scatter(data_result['인구수'], data_result['소계'],
            c= data_result['오차'], s=50)
# 회귀선
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98,
             df_sort.index[n], fontsize=15)

plt.xlabel('인구수')
plt.ylabel('인구당 비율')
plt.colorbar() 
plt.grid()
plt.show()


































