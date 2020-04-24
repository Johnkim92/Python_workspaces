# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:12:29 2020

@author: USER
"""
# BeautifulSoup 기본사용

# 예제로 사용할 html문서 카페에서 가져옴

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# soup.prettify() : html문서의 계층 구조를 알기 쉽게 보여준다.ㅣ
print(soup.prettify())

# title 태그를 반환
soup.title
print(soup.title)

# title태그의 이름('title')을 반환
soup.title.name
print(soup.title.name)

# title 태그의 문자열을 반환
soup.title.string

# title 태그의 부모 태그의 이름을 반환
soup.title.parent.name

# 첫 p태그를 반환 
soup.p

# 'class'속성이 있는 첫 p태그를 반환
soup.p['class']

# 모든 a태그를 리스트 형태로 반환
soup.find_all('a')

# soup.find(): 설정한 값에 해당하는 태그를 반환.
# id가 'link3'인 태그를반환
soup.find(id="link3")

# get(): 지정한 속성을 반환
for link in soup.find_all('a'):
    print(link.get('href'))
    
# get_text(): html문서 내의 텍스트를 반환
print(soup.get_text())


# Requests 기본 사용
'''
html 소스 가져오기
Requests를 사용하면 아래와 같이 간단한 코드만으로 웹페이지의
html 소스를 가져올 수 있다.
'''

import requests

# requests.get()에 의한 response에는 다양한 정보가 포함되어ㅣ이싿.
r = requests.get('https://google.com')
html = r.text
print(html)

'''
웹 페이지의 content를 유니코드 형태가 아니라 bytes형태로 얻기 위해서는
r.text가 아닌 r.content를 사용할 수도 있다.
'''
html = r.content
print(html)


# response 객체 : requests.get()의 반환 객체
'''
response 객체는
HTTP request에 의한 서버의 응답 정보를 가지고 있다.
status_code, headers, encoding, ok 등의 속성을 이용하면
다양한 정보를 얻을 수 있다.
'''

print(r.status_code)
print(r.headers['Content-Type'])
print(r.encoding)
print(r.ok)

'''
status_code는 정상일 경우 200, 페이지가 발견되지 않을경우 400
encoding방식은 ISO-8859-1이고, 요청에 대한 응답이 정상적으로 이루어졌음을 
알 수 있다.
ok는 status_code가 200보다 작거나 같은경우 True 그렇지 않으면 False이다.
'''

'''
만약 인코딩 방식이 달라서 한글이 제대로 표시 되지 않으면
아래와 같이 인코딩 방식을 변경.
'''
r.encoding='utf-8'

'''
Requests를 이용해서 html소스를 가져왔지만,
단순한 문자열 형태이기 때문에 파싱(Parsing)에 적합하지 않다.
그렇기 때문에 BeautifulSoup 을 이용해서
파이썬이 html 소스를 분석하고 데이터를 추출시키기 편리하도록 객체로 변환
'''

