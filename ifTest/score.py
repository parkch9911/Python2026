name = input("이름 :")
sub1 = int(input("국어 :"))
sub2 = int(input("영어 :"))
sub3 = int(input("수학 :"))
total = sub1+sub2+sub3
avg = total
print("-"*40)
print(f"총점 :{total}점")
print(f"평균 :{avg:.2f}점")
if sub1 < 40 or sub2 < 40 or sub3 < 40:
    print("과락")
elif total >= 90:
    print("학점 : A")
elif total >= 80:
    print("학점 : B")
elif total >= 70:
    print("학점 : C")
elif total >= 60:
    print("학점 : D")
else:
    print("학점 : F")





