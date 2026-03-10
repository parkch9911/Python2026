name = input("이름을 입력하세요 : ")
pay = int(input("시급을 입력하세요 : "))
hour = int(input("하루 근무시간을 입력하세요(h) : "))
workDay = int(input("근무일수을 입력하세요(d) : "))
startWork = int(input("근무 시작 시간을 입력하세요(24h) : "))
weekWork = hour*workDay
hpay = 0

print("="*60)
print("급여명세서")
print("="*60)
print(f"이름 : {name}")
print(f"시급 : {pay}")
print(f"근무시간 : {weekWork}시간 ({hour}x{workDay}일)")
if startWork >= 22 or startWork <= 6:
    uppay=pay*1.5
    print(f"야간 근무 : 해당있음 (시급{int(uppay):,}원 적용)")
else:
    print(f"야간 근무 : 해당없음 (시급{pay}원 적용)")
if weekWork >= 15:
    hpay=1
    print("주휴수당 : 해당있음")
else:
    print("주휴수당 : 해당없음")
print("="*60)
print(f"기본급 : {int(weekWork*uppay):,}원")
if hpay == 1:
    total =(weekWork*uppay)+(hour*uppay)
    print(f"주휴수당 : {int(hour*uppay):,}원")
else:
    print(f"주휴수당 : {0}원")
    total =(weekWork*pay)+(hour*pay)
print(f"세금(3.3%) : {int((total/100)*3.3):,}원")
tax = (total//100)*3.3
print("="*60)
print(f"실수령액 : {int(total-tax):,}원")


