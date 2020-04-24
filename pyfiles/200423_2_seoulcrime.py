# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:33:34 2020

@author: USER
"""

# =============================================================================
#  강남 3구는 안전한가?
# =============================================================================
'''
강남 3구의 주민들이 자신들이 거주하는 구의 체감 안전도를
높게 생각한다는 기사를 확인해 보도록 한다.
기사 원문 http://news1.kr/articles/?1911504

Matplotlib의 heatmap 등을 그릴 때
cmap의 디폴트 설정이 변경되어 heatmap 등에서 cmap을 적용할 때
옵션을 잡아주어야 동일한 효과가 나타난다.

Folium이 0.4.0으로 버전업되면서
choropleth 명령에서 geo_str 옵션명이 geo_data옵션명으로 변경됨.
circle marker 적용할 때 fill=True옵션을 반드시 사용해야함.
'''

##
# 데이터 정리하기
# 필요한 모듈을 import
import numpy as np
import pandas as pd
'''
다운받은 데이터(csv) 파일을 읽는다.
콤마로 천단위가 구분되어 있고 한글 인코딩은 euc-kr
'''
crime_and_police = pd.read_csv('../datas_and_pics/datas/02. crime_in_Seoul.csv', thousands=',',encoding='euc-kr')
r = crime_and_police.head()

'''
관서별로 되어 있는 데이터를 소속 구별로 변경
1. 경찰서 이름으로 구 정보 얻기
'''

# 구글 맵스를 사용해서 경찰서의 위치(위도, 경도) 정보를 받아온다.
import googlemaps

# 자신의 key를 사용
gmaps_key = '본인의 API키를 사용하세요!!'
gmaps = googlemaps.Client(key=gmaps_key)
r = gmaps.geocode('서울중부경찰서', language='ko')
print(r)


# 중부서, 수서서 -> 서울**경찰서로 변경
station_name = []
for name in crime_and_police['관서명']:
    station_name.append('서울'+ str(name[:-1])+'경찰서')
    
print(station_name)

# 경찰서 이름을 이용하여 주소 얻기
station_addreess = []
station_lat = []
station_lng = []

for name in station_name:
    tmp = gmaps.geocode(name, language='ko')
    station_addreess.append(tmp[0].get("formatted_address"))
    tmp_loc = tmp[0].get("geometry")
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    print(name + '-->'+tmp[0].get("formatted_address"))
    
print(station_addreess)

'''
저장한 주소를 띄어쓰기, 공백으로 나누고,
구별이라는 컬럼으로 저장
'''
gu_name=[]

for name in station_addreess:
    tmp = name.split()
    tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
    
    gu_name.append(tmp_gu)
    
crime_and_police['구별'] = gu_name
print(crime_and_police.head())

'''
금천경찰서의 경우 관악구로 되어 있어서
금천구로 변경
'''

crime_and_police[crime_and_police['관서명']=='금천서']
crime_and_police.loc[crime_and_police['관서명']=='금천서', ['구별']]='금천구'
crime_and_police[crime_and_police['관서명']=='금천서']

crime_and_police.to_csv('../datas_and_pics/datas/02_crime_in_Seoul_include_gu_name.csv')
crime_anal_raw = pd.read_csv('../datas_and_pics/datas/02_crime_in_Seoul_include_gu_name.csv')
# pandas의 pivot_table
'''
pd.pivot_table(df, index=[], columns=[], values=[], aggfunc=[], fill_value=0, margins=True)
옵션 설명 
1. 피벗 테이블을 만들기 위한 기본 데이터
2. pivot_table의 index를 설정(multi index도 가능)
3.원하는 칼럼을 설정
4. 컬럼에 해당하는 값
5. 분석을 위한 파라미터 예) np.sum, np.mean 사용
6. fill_value = 0 NAN값을 채우기
7. 모든 데이터의 결과를 아래에 붙일 것인지 설정

피벗테이블은 컬럼을 인덱스화 시켜서 나머지 값들을 재정렬시켜준다.
'''

crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)
crime_anal.head()
print(crime_anal)

'''
각 범죄별 검거율을 계산하고,
검거 건수는 검거율로 대체한 후 검거 건수는 삭제
'''
crime_anal['강간검거율'] = crime_anal['강간 검거']/crime_anal['강간 발생']*100
crime_anal['강도검거율'] = crime_anal['강도 검거']/crime_anal['강도 발생']*100
crime_anal['살인검거율'] = crime_anal['살인 검거']/crime_anal['살인 발생']*100
crime_anal['절도검거율'] = crime_anal['절도 검거']/crime_anal['절도 발생']*100
crime_anal['폭력검거율'] = crime_anal['폭력 검거']/crime_anal['폭력 발생']*100

del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

print(crime_anal.head())

'''
100이 넘는 숫자들은 100으로 처리
'''
con_list = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']

for column in con_list:
    crime_anal.loc[crime_anal[column] > 100 , column] = 100

print(crime_anal.head())

# 칼럼 뒤에 발생이라는 단어 삭제 : rename()를 사용
crime_anal.rename(columns ={'강간 발생' : '강간',
                            '강도 발생' : '강도',
                            '살인 발생' : '살인',
                            '절도 발생' : '절도',
                            '폭력 발생' : '폭력',
                            }, inplace=True)

####################
# 데이터 표현을 위해 전처리
'''
강도와 살인은 두 자릿수
절도와 폭력은 네 자릿수로 구성 되어 있어
각각을 비슷한 범위에 놓고 비교하는 것이 편리하기 때문에
각 컬럼별로 정규화 작업

각 항목의 최대값을 1로 두면,
추후 범죄 발생 건수를 종합적으로 비교할 때 편리

강간, 강도, 살인, 절도, 폭력에 대하여
각 컬럼별로 정규화
'''

'''
파이썬의 머신러닝에 관한 모듈중
scikit learn 에 있는 전처리 도구에는
최소, 최대값을 이용하여 정규화 시키는 함수가 존재 : MinMaxScaler()
'''
from sklearn import preprocessing

col = ['강간','강도','살인','절도','폭력']

x = crime_anal[col].values
min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x.astype(float))

crime_anal_norm = pd.DataFrame(x_scaled, columns=col,
                               index = crime_anal.index)

# 정규화된 데이터프레임에 검거율 추가
col2 = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm[col2] = crime_anal[col2]
print(crime_anal_norm.head())

# CCTV_result.csv에서 구별 인구수와 CCTV 갯수만 추가
result_CCTV = pd.read_csv('../datas_and_pics/datas/01. CCTV_result.csv',
                          encoding='utf-8', index_col = '구별')
crime_anal_norm[['인구수','CCTV']]=result_CCTV[['인구수','소계']]
print("인구수와 CCTV 개수 => ",crime_anal_norm.head())

# 발생 건수의 합을 '범죄'라는 컬럼으로 합하여 추가
col = ['강간','강도','살인','절도','폭력']
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis=1)
print("범죄라는 컬럼으로 합 => ",crime_anal_norm.head())

# 검거율도 통합하여 추가
col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm['검거율'] = np.sum(crime_anal_norm[col], axis=1)
print("검거율도 통합 => ", crime_anal_norm.head())

import matplotlib.pyplot as plt
import seaborn as sns  # 다수의 상관관계 표현하기 위한 모듈
import platform   # 한글 폰트 설정하기 위한 모듈

# pairplot() 상관관계 : '강도', '살인', '폭력'
sns.pairplot(crime_anal_norm, vars = ["강도","살인","폭력"], kind='reg', size = 3)
plt.show()
'''
강도와 폭력, 살인과 폭력, 강도와 살인 모두 양의 상관관계를 보임.
'''

# pairplot() 상관관계 : '인구수', 'CCTV', '살인', '강도'
sns.pairplot(crime_anal_norm, x_vars = ["인구수", "CCTV"],
             y_vars=["살인","강도"], kind='reg', size=3)
plt.show()
'''
전체적인 상관계수는 CCTV와 살인의 관계가 낮을지는 몰라도
CCTV가 없을 때 살인 사건이 많은 구간이 있다.
즉, CCTV수를 기준으로 좌측면에 살인과 강도의 높은 수를 갖는 데이터가 보인다.
'''

# pairplot() 상관관계 : '인구수', 'CCTV', '살인검거율', '강도검거율'
sns.pairplot(crime_anal_norm, x_vars = ["인구수", "CCTV"],
             y_vars=["살인검거율","강도검거율"], kind='reg', size=3)
plt.show()


# pairplot() 상관관계 : '인구수', 'CCTV', '살인검거율', '강도검거율'
sns.pairplot(crime_anal_norm, x_vars = ["인구수", "CCTV"],
             y_vars=["절도검거율","강도검거율"], kind='reg', size=3)
plt.show()

'''
인구수와 검거율에는 차이가 없음을 알 수 있다.
그러나 CCTV의 경우엔 음의 상관관계를 보이고 있다.
이말은 즉 CCTV가 적어도 검거율이 높음을 알 수 있다.
'''

# 검거율의 합계인 검거 항목 최고 값을 100으로 한정 한 후,
# 그 값으로 정렬
tmp_max = crime_anal_norm['검거율'].max()
crime_anal_norm['검거율'] = crime_anal_norm['검거율'] / tmp_max * 100
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거율', ascending=False)
crime_anal_norm_sort.head()

# heatmap으로 시각화
target_col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거율', ascending=False)
plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col], annot=True,
            fmt = 'f', linewidths=.5,
            cmap='RdPu')
plt.title('범죄 검거 비율 (정규화된 검거의 합으로 정렬)')
plt.show()

# 발생 건수 정렬하여 heatmap으로 시각화
target_col =['강간','강도','살인','절도','폭력']
crime_anal_norm['범죄'] = crime_anal_norm['범죄']/5

crime_anal_norm_sort = crime_anal_norm.sort_values(by='범죄', ascending=False)

plt.figure(figsize=(10,10))

sns.heatmap(crime_anal_norm_sort[target_col],
            annot=True, fmt = 'f',
            linewidths=.5,
            cmap='RdPu')
plt.title('범죄비율 (정규화된 발생 건수로 정렬)')
plt.show()

# 중간 저장
crime_anal_norm.to_csv('../datas_and_pics/datas/02_crime_in_Seoul_final.csv', sep=',',
                       encoding='utf-8')

import json
geo_path = '../datas_and_pics/datas/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

crime_anal_raw['lat'] = station_lat
crime_anal_raw['lng'] = station_lng

col = ['살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거']
tmp = crime_anal_raw[col]/crime_anal_raw[col].max()

crime_anal_raw['검거'] = np.sum(tmp, axis=1)
crime_anal_raw.head()

import folium
import webbrowser

map = folium.Map(location=[37.5502, 126.982], zoom_start=11)
for n in crime_anal_raw.index:
    folium.Marker([crime_anal_raw['lat'][n],
                   crime_anal_raw['lng'][n]]).add_to(map)
    
map
map.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")

map = folium.Map(location=[37.5502, 126.982], zoom_start=11)
for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n],crime_anal_raw['lng'][n]],
                   radius=crime_anal_raw['검거'][n]*10,
                   color='#3186cc',
                   fill_color='#3186cc',
                   fill=True).add_to(map)
map
map.save('folium_kr2.html')
webbrowser.open_new("folium_kr2.html")

############################

map = folium.Map(location=[37.5502, 126.982], zoom_start=11)
map.choropleth(geo_data=geo_str,
               data=crime_anal_norm['범죄'],
               columns=[crime_anal_norm.index, crime_anal_norm['범죄']],
               fill_color='PuRd',
               key_on = 'feature.id')
  # PuRd, YlGnBu
for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n],crime_anal_raw['lng'][n]],
                   radius=crime_anal_raw['검거'][n]*10,
                   color='#3186cc',
                   fill_color='#3186cc',
                   fill=True).add_to(map)

map
map.save('folium_kr3.html')
webbrowser.open_new("folium_kr3.html")


# 서울시 외국인 인구 데이터 구별로 히트맵
data_result= pd.read_csv('../datas_and_pics/datas/data_result.csv')
data_result1 = data_result.set_index(data_result['구별'])

map = folium.Map(location=[37.5502, 126.982], zoom_start=11)
map.choropleth(geo_data = geo_str,
               data = data_result1['외국인'],
               columns = [data_result1.index,data_result1['외국인']],
                fill_color='YlGn',fill_opacity=0.7,line_opacity=0.2,
               key_on = 'feature.id')

map
map.save('folium_kr4.html')
webbrowser.open_new("folium_kr4.html")





