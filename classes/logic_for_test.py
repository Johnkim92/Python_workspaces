a, b = input("시작할 숫자와 끝나는 범위를 띄어쓰기로 구분하여 입력해 주세요 : ").split()
a = int(a)
b = int(b)

if(a%2 == 0):
    a = a+1
else:
    a = a

for i in range(a, b, 2):
    print(i)
