total = 0
max = 0
min = 0
maxDay=""
minDay=""
cnt = 0
want = int(input("목표 일 매출액 : "))
for i in ["월","화","수","목","금","토","일"]:
    daySale = int(input(f"{i}요일 매출 : "))
    if daySale > max:
        max = daySale
        maxDay = i
    if i == "월":
        min = daySale
        minDay = i
    if daySale < min:
        min = daySale
        minDay = i
    total = total+daySale
    if daySale >= want:
        print("→   목표 달성")
        cnt += 1
    elif daySale < want and daySale >= (want/100)*70:
        print("→   분발 필요")
    else:
        print("→   목표 미달")
    
print(f"총 매출액 : {(total):,}원 | 일 평균 : {(total//7):,}원(정수처리)")
print(f"최고 매출 :{maxDay}요일 {(max):,}원 | 최저 매출 : {minDay}요일 {(min):,}원")
print(f"목표 달성 : {cnt}일")

