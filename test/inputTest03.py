name = input("이름을 입력하세요 : ")
height = float(input("키를 입력하세요(cm) : "))
weight = float(input("몸무게를 입력하세요(kg) : "))
commonWeight = (height-100)*0.9
bmi = weight/commonWeight*100
print("="*40)
print(f"{name}님의 비만도는 {bmi:.2f}% 입니다.")
print("="*40)
