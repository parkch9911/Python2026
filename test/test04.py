# input ("안내 문구") : 키보드로부터 값 입력받는다.
# 단, input()으로 입력받은 모든 값은 문자열로 취급된다.
# 계산이 필요한 정수나 실수는 반드시 int로 형변환을 해야한다.
# int(input("국어점수:"))
var = int(input("첫번째 정수 입력:"))
var2 = int(input("두번째 정수 입력:"))
print("="*20)
print(f"합 {var}+{var2} =",var+var2)
print(f"차 {var}-{var2} =",var-var2)
print(f"곱 {var}*{var2} =",var*var2)
print(f"분 {var}/{var2} =",var/var2)
print("="*20)

