pay = 0
totalDiscount = 0
total = 0
cnt = 0

while True:
    grade = input("회원 등급 (END 종료) : ").upper()
    if grade == "VIP":
        purchase = int(input("구매금액 : "))
        print(f"할인금액 : {int((purchase/100)*20)+10000}원 → 결제금액 : {int(purchase-(((purchase/100)*20)+10000))}원")
        total += purchase
        totalDiscount += ((purchase/100)*20)+10000
        pay += purchase-(((purchase/100)*20)+10000)
        cnt +=1
    elif grade == "GOLD":
        purchase = int(input("구매금액 : "))
        print(f"할인금액 : {int((purchase/100)*10)+5000}원 → 결제금액 : {int(purchase-(((purchase/100)*10)+5000))}원")
        total += purchase
        totalDiscount += ((purchase/100)*10)+5000
        pay += purchase-(((purchase/100)*10)+5000)
        cnt +=1
    elif grade == "SILVER":
        purchase = int(input("구매금액 : "))
        print(f"할인금액 : {int((purchase/100)*5)}원 → 결제금액 : {int(purchase-((purchase/100)*5))}원")
        total += purchase
        totalDiscount += ((purchase/100)*5)
        pay += purchase-((purchase/100)*5)
        cnt +=1
    elif grade == "BRONZE":
        purchase = int(input("구매금액 : "))
        print(f"할인금액 : {int((purchase/100)*0)}원 → 결제금액 : {int(purchase-((purchase/100)*0))}원")
        total += purchase
        totalDiscount += ((purchase/100)*0)
        pay += purchase-((purchase/100)*0)
        cnt +=1
    elif grade == "END":
        print("---전체주문요약---")
        print(f"주문 건수 : {cnt}건")
        print(f"총 주문 금액 : {total}원 | 총 할인 금액 : {totalDiscount}원 | 총 결제 금액 : {pay}원")
        break