transactions = [
['2024-01', 3200000],
['2024-01', 1500000],
['2024-02', 2800000],
['2024-02', 900000],
['2024-03', 4100000],
['2024-03', 2200000],
['2024-04', 1800000],
['2024-04', 3300000],
['2024-05', 5000000],
['2024-06', 2100000]
]
dupl={}
for i in transactions:
    month=i[0]
    amount=i[1]
    if month not in dupl: # 날짜가 month 배열에 존재하지않으면 
        dupl[month] = amount
    else:
        dupl[month] +=amount

max = 0
min = False
avg = 0
print("==월별매출==")
for oneList in dupl:
    print(f"{oneList} : {(dupl[oneList]):,}원")
    if dupl[oneList] > max:
        max = dupl[oneList]
        maxDay = oneList 
    if min == False:
        min = dupl[oneList]
        minDay = oneList
    if dupl[oneList] < min:
        min = dupl[oneList]
        minDay = oneList
    avg += dupl[oneList]/len(dupl)
print()

print(f"최고 월 매출 : {maxDay} ({(max):,}원)")
print(f"최저 월 매출 : {minDay} ({(min):,}원)")
print(f"월 평균 매출 : {int(avg):,}원")





