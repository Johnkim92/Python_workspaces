# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:40:28 2020

@author: USER
"""
# 한줄 실행 단축키 : F9

import sqlite3 as sql
print(sql.version)
print(sql.sqlite_version)
con = sql.connect("c:/acon_python/kospi.db")
print(type(con))
cursor = con.cursor()
# 객체에 connect 저장
cursor.execute("CREATE TABLE KAKAO(Date text, Open int, High int, Low int, Closing int, Volumn int)")
cursor.execute("INSERT INTO KAKAO VALUES('16.06.06',97000,98600,96900,98000,321405)")
cursor.execute("SELECT * FROM KAKAO")
print(cursor.fetchone())
print(cursor.fetchone())
print(len(cursor.fetchall()))
print(cursor.fetchmany(3))
kakao = cursor.fetchall()
con.commit()
con.close()
print(kakao[0][0])
print(kakao[1][0])
