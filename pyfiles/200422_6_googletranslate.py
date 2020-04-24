# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:05:23 2020

@author: USER
"""

# Numpy 난수 생성 (Random 모듈)
# 난숫 생성에 활용할 수 있는 Numpy의 random 모듈 (numpy.random)

# 1 - random.rand() : 주어진 형태의 난수를 생성
import numpy as np

# 예제 1
'''
만들어진 난수 array는 주어진 값에 의해 결정되며,
[0,1) 범위에서 균일한 분포를 갖는다.
'''

a = np.random.rand(5)
print(a)

'''
random.rand() 주어진 형태의 난수 array를 생성
random.randint() [최저값, 최대값)의 범위에서 임의의 정수
random.randn() 표준 정규분포를 갖는 난수를 반환
random.standard_normal() :  randn()과 standard_normal()은 기능이 비슷
하지만 튜플을 인자로 받는 점에서 차이가 있다.
random.random_sample(): [0.0, 1.0) 범위의 임의의 실수를 반환
random.choice(): 주어진 1차원 어레이에서 임의의 샘플을 생성
random.seed(): 난수 생성에 필요한 시드를 정한다.코드를 실행할 때마다 똑같은
난수가 생성.
'''

#Matplotlib 산점도 그리기
# scatter()를 이용해서 산점도를 그릴 수 있다.
import matplotlib.pyplot as plt

'''
np.random.seed()를 통해서 난수 생성의 시드를 설정하면,
같은 난수를 재사용 할 수 있다.
seed()에 들어갈 파라미터는 0에서 4294967295사이의 정수여야한다.
'''
np.random.seed(19680801)


# 1 - random.rand() : 주어진 형태의 난수를 생성.

b = np.random.rand(2,3)
print(b)

'''
x, y의 위치, 마커의 색(colors)과 면적(area)을 무작위로 지정

예를들어 x는
0에서 1사이의 무작위한 50개의 값을 갖는다.
'''
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30*np.random.rand(N))**2

'''
scatter()에 x, y 위치를 입력
s는 마ㅌ커의 면적을
c는 마커의 색을 지정
alpha는 마커색의 투명도를 결정
'''
plt.scatter(x,y,s=area, c=colors, alpha=0.5)
plt.show()

# Matplotlib 히스토그램 그리기
# hist() 를 이용해서 히스토그램을 그리기

# 1 - 값 입력하기

#weight 리스트는 몸무게 값을 나타낸다.
weight = [68,81,64,56,78,74,61,77,66,68,59,
          71,80,59,67,81,69,73,69,47,70,65]

# hist() 함수에 리스트의 형태로 값들을 직접 입력해주면 된다.
plt.hist(weight)
plt.show

# 2 - 여러 개의 히스토그램 그리기

'''
Numpy의 np.random.randn()와
np.random.standard_normal(), np.random.rand()함수를 이용해서
임의의 값들을 생성.
'''

# array a는 표준 편차 2.0, 평균 1.0을 갖는 정규 분포
a = 2.0*np.random.randn(10000)+1.0

# array b는 표준 정규 분포를 따른다.
b = np.random.standard_normal(10000)

# array c는 -10.0에서 10.0 사이의 균일한 분포를 갖는 5000개의 임의의 값.
c = 20.0*np.random.rand(5000) - 10.0

'''
세 개의 분포를 동시에 그래프에 나타내기.
plt.hist()

bins는 몇개의 영역으로 쪼갤지를 설정.
density = True 로설정 해주면,
밀도 함수가 되어서 막대의 아래 면적이 1이된다.
alpha는 투명도를 의미한다. 0.0~1.0의 값을 갖는다.
histtype을 'step'으로 설정하면 막대 내부가 비어있고,
'stepfilled'로 설정하면 막대 내부가 채워진다.
'''

plt.hist(a, bins=100, density=True, alpha=0.7, histtype='step')
plt.hist(b, bins=50, density=True, alpha=0.5, histtype='stepfilled')
plt.hist(c, bins=100, density=True, alpha=0.9, histtype='step')
plt.show()

a = np.random.rand(1000)
b = np.random.rand(10000)
c = np.random.rand(100000)

plt.hist(a, bins=100, density=True, alpha=.5, histtype='step', label='n=1000')
plt.hist(b, bins=100, density=True, alpha=.75, histtype='step', label='n=10000')
plt.hist(c, bins=100, density=True, alpha=1.0, histtype='step', label='n=100000')
plt.show()

# a는 [0,10) 범위의 임의의 정수 1000개
a = np.random.randint(0,10,1000)
b = np.random.randint(10, 20, 1000)
c = np.random.randint(0, 20, 1000)

plt.hist(a, bins=100, density=False, alpha=.5, histtype='step', label='0<=randint<10')
plt.hist(b, bins=100, density=False, alpha=.75, histtype='step', label='10<=randint<20')
plt.hist(c, bins=100, density=False, alpha=1.0, histtype='step', label='0<=randint<20')
plt.legend()
plt.show()

# Matplotlib 3차원 산점도 그리기
'''
scatter() 를 이용해서 3차원 산점도를 그리기
3차원 그래프를 그리기 위해서
from mpl_toolkits.mplot3d import Axes3D 를 추가
이 부분은 matplotlib 3.1.0 버전부터는
디폴트로 포함되기 때문에 적어주지 않아도 된다.
'''
from mpl_toolkits.mplot3d import Axes3D

n = 100
xmin, xmax, ymin, ymax , zmin, zmax = 0,20,0,20,0,50
cmin, cmax = 0,2
xs = (xmax-xmin)*np.random.rand(n)+xmin
ys = (xmax-xmin)*np.random.rand(n)+ymin
zs = (xmax-xmin)*np.random.rand(n)+zmin
color = (xmax-xmin)*np.random.rand(n)+cmin

# rcParams 를 이용해서 figure의 사이즈를 설정
plt.rcParams["figure.figsize"] = (6,6)
fig = plt.figure()

'''
3D axes를 만들기 위해
add_subplot() 에 projection='3d' 키워드를 입력
'''
ax = fig.add_subplot(111, projection='3d')

'''
scatter() 함수에 x,y,z 위치를 array의 형태로 입력
마커의 형태를 원형으로 설정
cmap='Greens' 를 통해 colormap을 녹색 계열로 설정
'''

ax.scatter(xs,ys,zs, c=color, marker='o',s = 15, cmap='Greens')

### Googletrans - 파이썬을 위한 구글 번역 API ###
'''
Googletrans는 
구글 번역 API를 구현한 파이썬라이브러리

파이썬과 Googletrans를 이용해서
무료로 그리고 무제한으로 구글의 번역 기능을 사용할 수 있다.
'''

### Googletrans 기본 사용 ###
'''
Googletrans 라이브러리를 이용해서
간단한 문장을 특정 언어로 (구글) 번역하고,
언어를 자동 감지하는 기능을 사용
'''

# 1. 번역하기
# googletrans 에서 Translator 불러오기

from googletrans import Translator

translator = Translator()


# translate() 에 번역할 문장을 입력해주면 아래 같은 결과를 출력.
print(translator.translate('안녕하세요'))
'''
Translated 객체는 번역이 이루어진 결과를 나타내는 객체.
'''

# translator.translate('안녕하세요').text를 출력하면 번역된 문장이 출력
print(translator.translate('누런색', dest='en').text)

print(translator.translate('안녕하세요', src='ko', dest='zh-cn').pronunciation)

































