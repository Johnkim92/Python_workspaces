# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:31:46 2020

@author: USER
"""


# =============================================================================
#   Pandas를 사용한 데이터 분석 기초
# =============================================================================

'''
분석할 데이터의 양이 커지고
데이터의 입출력 속도가 빨라지고
데이터의 종류가 다양해 짐에 따라
기존보다 데이터를 분석하기 어려워졌고
이로 인해 데이터 분석 분야가 업계의 주목을 받는다.

빅데이터
양 속도 다양성의 세 가지 V를 가진 데이터

빅데이터 분석에는
다양한 프로그래밍 언어와 기술이 사용되고 있는데 파이썬도 그중 하나이다.

파이썬이 오픈 소스 기반의 통계언어인 R과 더불어
빅데이터 분석 분야에서 인기가 높아진 것은 여러 가지 이유가 있지만,
Pandas라는 라이브러리 덕이 크다.
'''

# =============================================================================
#   Pandas Series
# =============================================================================
'''
파이썬이 인기 있는 이유 중 하나는
파이썬의 기본 자료구조인 리스트, 튜플, 딕셔너리가 사용하기 편리하며
데이터를 다루는 데 효과적이기 때문이다.

Pandas역시 효과적인 데이터 분석을 위한
고수준의 자료구조와 데이터 분석 도구를 제공

Pandas의
Series는 1차원 데이터를 다루는 데 효과적인 자료구조이며,
DataFrame은 행과 열로 구성된 2차원 데이터를 다루는 데 효과적인 자료구조이다.

Pandas를 이해하려면
가장먼저 Pandas의 핵심 자료구조인 Series와 DataFrame을 알아야 한다.
'''

# =============================================================================
#   파이썬 리스트, 튜플, 딕셔너리
# =============================================================================
# 리스트
mystock = ['kakao','naver']
print(mystock[0])
print(mystock[1])
for stock in mystock:
    print(stock)
print(' ')   
# 튜플
'''
튜플은
리스트의 []와 달리 ()를 사용.
수정이 가능한 리스트와 달리 수정할 수 없다.
대신 리스트에 비해서 속도가 빠르다는 장점이 있다.

그래서 원소를 한 번 넣은 후에
수정할 필요가 없으며
속도가 중요한 경우에 리스트 대신 튜플 사용
'''

# 딕셔너리
exam_dic = {'key1':'room1','key2':'room2'}
print(exam_dic['key1'])
print(exam_dic['key2'])
print(' ')
# 리스트와 딕셔너리
kakao_daily_ending_prices =[92300,94300,92100,92400,92600]
for price in kakao_daily_ending_prices:
    print(price)
    
kakao_daily_ending_prices = {'2016-02-19':92600,
                             '2016-02-18':92400,
                             '2016-02-17':92100,
                             '2016-02-16':94300,
                             '2016-02-15':92300}
print(kakao_daily_ending_prices['2016-02-19'])
print(' ')

# =============================================================================
#   Series 기초
# =============================================================================
'''
Pandas의 Series는 1차원 배열과 같은 자료 구조.
파이썬 리스트와 튜플도 1차원 배열과 같은 자료 구조

사실 Pandas의 Series는
어떤 면에서는 파이썬의 리스트와 비슷하고
어떤 면에서는 파이썬의 딕셔너리와 닮은 자료 구조
'''

'''
Series를 사용하기에 앞서
Pandas라는 모듈에서 직접 Series와 DataFrame을
로컬 네임스페이스로 import
'''
import pandas as pd
print(pd.Series)
'''
Series를 직접 로컬 네임스페이스로 import한 경우에는 pandas는 생략하고
바로 Series라고만 적으면 된다.
'''
from pandas import Series, DataFrame

kakao = Series([92600,92400,92100,94300,92300])
print(kakao)
print(type(kakao))
print(type(kakao[1]))
print(' ')
# Series는 리스트 형태 구조를 가지고 있지만 해당 번호에 대한 index번호도 같이 저장되어
# 딕셔너리 구조를 갖고 있다.
'''
시리즈 객체는
일차원 배열과 달리 값 뿐만 아니라
각 값에 연결된 인덱스 값도 동시에 저장

시리즈 객체 생성시에
인덱스 값을 따로 지정하지 않으면
기본적으로 Series객체는 0부터 시작하는 정수값을 사용하여 인덱싱.
'''
kakao2 = Series([92600,92400,92100,94300,92300], index=['2016-02-19',
                                                        '2016-02-18',
                                                        '2016-02-17',
                                                        '2016-02-16',
                                                        '2016-02-15'])
'''
kakao2 라는 시리즈 객체는
인덱스 값으로 날짜에 해당 하는 문자열을 지정했기 때문에 정숫값으로 인덱싱 하는 것
대신 날짜를 의미하는 문자열을 사용하여 각 날짜에 대한 종가를 바로 얻어올 수 있다.
'''
print(type(kakao2['2016-02-16']))

'''
시리즈 객체의 index와 values라는 이름의 속성을 통해 접근할 수 있다.
'''
for date in kakao2.index:
    print(date)
print(' ')
for ending_price in kakao2.values:
    print(ending_price)
print(' ')    

'''
Pandas의 Series는
서로다르게 인덱싱된 데이터에 대해서도 알아서 덧셈연산을 처리해준다.
'''
mine = Series([10,20,30], index=['naver','sk','k'])
friend = Series([40,50,60], index=['kt','naver','sk'])
merge = mine + friend
print(merge)
print(' ')

# =============================================================================
#  Pandas DataFrame
# =============================================================================
'''
Pandas의 Series가 1차원 형태의 자료구조라면
DataFrame은 여러 개의 칼럼으로 구성된 2차원 형태의 자료구조

Pandas의 DataFrame을 사용하면 로우와 칼럼으로 구성된 2차원 구조의 데이터를
쉽게저장하고 조작할 수 있다.
'''

# DataFrame 생성
'''
DataFrame 객체를 생성하는 가장 쉬운 방법은 파이썬의 딕셔너리를 사용하는 것
딕셔너리를 통해 각 칼럼에 대한 데이터를 저장한 후,
딕셔너리를 DataFrame 클래스의 생성자 인자로 넘겨주면 객체가 생성된다.
'''
raw_data ={'col0':[1,2,3,4],'col1':[10,20,30,40],'col2':[100,200,300,400]}
data = DataFrame(raw_data)
print(data)
print(type(raw_data))
print(type(data))
print(' ')
'''
col0 col1 col2 라는 3개의 칼럼이 위에 존재한다.
이 문자열들은 DataFrame의 각 컬럼을 인덱싱하는데 사용된다.
로우방향으로는 Series와 유사하게 정수값으로 자동 인덱싱된 것을 확인 할 수 있다.
'''

'''
DataFrame에 있는 각 컬럼은 시리즈 객체임을 알 수 있다.
즉 DataFrame은 인덱스가 같은 여러개의 Series객체로 구성된 자료 구조이다.
data라는 변수가 바인딩하는 DataFrame에는 3개의 Series 객체가 있다.
이는 키에 각각 대응 되는 값이고 이것들 하나의 파이썬 딕셔너리 객체로 생각하면된다.
따라서 key를 통해 value에 해당하는 Series 객체에 접근할 수 있다.
'''
daeshin={'open':[11650,11100,11200,11100,11000],
         'high':[12100,11800,11200,11100,11150],
         'low':[11600,11050,10900,10950,10900],
         'close':[11900,11600,11000,11100,11050]}
daeshin_day = DataFrame(daeshin)
print(daeshin_day)
print(' ')
'''
DataFrame객체에서 칼럼의 순서는 DataFrame객체를 생성할 때 columns라는 키워드를 지정할 수 있다.
'''
daeshin_day2 = DataFrame(daeshin, columns=['CLOSE','OPEN','HIGH','LOW'])
print(daeshin_day2)
print(' ')
date = ['20.02.29','20.02.26','20.02.25','20.02.24','20.02.23']
daeshin_day3 = DataFrame(daeshin, columns=['open','high','low','close'], index=date)
print(daeshin_day3)
print(' ')
# DataFrame 칼럼 로우 선택
'''
종가를 기준으로만 데이터를 분석한다면
'close'칼럼에 대한 데이터만을 DataFrame 객체로 부터 얻어낸다.
'''
close = daeshin_day3['close']
print(close)
'''
DataFrame객체의 칼럼이름과 인덱스값을 확인하려면 각각 columns와 index속성을 사용.
'''
print(daeshin_day3.columns)
print(daeshin_day3.index)
print(' ')