month = int(input("방문 월을 입력하세요 (1~12) : "))
adult = int(input("성인 인원수를 입력하세요 : "))
teen = int(input("청소년 인원수를 입력하세요 : "))
kid = int(input("어린이 인원수를 입력하세요 : "))
senior = int(input("경로 인원수를 입력하세요 : "))

peak = 0
count = adult+teen+kid+senior
discount = 0
discount2 = 0
print("="*60)

print("놀이공원 입장권 계산서")
if month == 7 or month == 8:
    print(f"방문월 : {month}월 (성수기)")
    peak = 1
else:
    print(f"방문월 : {month}월 (비수기 10%할인적용!)")
print("="*60)
print(f"성인 : {adult}명 : {(55000*adult):,}원")
print(f"청소년 : {teen}명 : {(40000*teen):,}원")
if kid >= 3:
    print(f"어린이 : {kid}명 : {0}원 (무료!)")
else:
    print(f"어린이 : {kid}명 : {(28000*kid):,}원")
print(f"경로 : {senior}명 : {(15000*senior):,}원")
if kid >= 3:
    total = (55000*adult)+(40000*teen)+(15000*senior)
else:
    total = (55000*adult)+(40000*teen)+(28000*kid)+(15000*senior)
print("="*60)
print(f"소계 : {(total):,}원")
if count >= 5:
    discount = (total//10)
    print(f"단체 할인 : -{(discount):,}원")
    if peak == 0:
        discount2 = (total//10)
        print(f"비성수기 할인 : -{(discount2):,}원")
        total = total-discount-discount2
elif peak == 0:
    discount = (total//10)
    print(f"비성수기 할인 : -{(discount):,}원")
    total = total - discount - discount2
    
print("="*60)
print(f"최종 금액 : {(total):,}원")
print("="*60)

print(f"총 인원 : {count}명")
print("="*60)