
# 문제 5-1

def myaverage(a,b):
    return (a+b)/2

# 문제 5-2

def get_max_min(data_list):
    return (max(data_list),min(data_list))

# 문제 5-3
import os

def get_txt_list(path):
    for x in os.listdir(path):
        if x.endswith('txt'):
            print(x)

# 문제 5-4

def check_bmi (weight, height):
    bmi = weight/((height)**2)
    if bmi < 18.5 :
        print('마른체형 입니다.')
    elif 18.5 <= bmi < 25.0 :
        print('표준입니다.')
    elif 25.0 <= bmi < 30.0:
        print('비만입니다.')
    else:
        print('고도 비만입니다.')

# 문제 5-5

def check_bmi2 ():
    weight = int(input('몸무게(kg)을 입력해주세요 : '))
    height = int(input('키(cm)를 입력해주세요 : '))
    bmi = weight/((height/100)**2)
    print('당신의 bmi값은 : ',bmi)
    if bmi < 18.5 :
        print('마른체형 입니다.')
    elif 18.5 <= bmi < 25.0 :
        print('표준입니다.')
    elif 25.0 <= bmi < 30.0:
        print('비만입니다.')
    else:
        print('고도 비만입니다.')

# 문제 5-6

def get_triangle_area(width, height):
    area = 0.5*width*height
    print(area)

# 문제 5-7

def add_start_to_end(start, end):
    a = (end*(end+1))/2
    if start > 1:
        b = (start*(start-1))/2
    else:
        b = 0
    print(int(a-b))

# 문제 5-8

def return3_char(data_list):
    for data in data_list:
        data = data[:3]
        print(data)

if __name__ == "__main__" :
    print(__name__)
    
