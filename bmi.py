weight = float(input("몸무게를 kg단위로 입력 하시오 : "))
height = float(input("키를 센티미터 단위로 입력하시오 : "))

bmi = (weight / ((height/100)**2))
print("당신의 BMI 는 ", bmi)

normal_weight = float(20 * ((height/100)**2))
print("당신의 정상 체중은 ", normal_weight)
