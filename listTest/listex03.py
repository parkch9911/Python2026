orders = [
{'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
{'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
{'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
{'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
{'id': 5, 'product': '웹캠','amount': 75000, 'status': 'PAID'}
]
paid=[]
total = 0
print("==결제완료 주문==")
for dict in orders:
    for item in dict:
        if item == "status" and dict[item] == "PAID":
            paid.append(dict)
for result in paid:
    print(f"{result["id"]}번 주문 / 상품 :{result["product"]} / 금액 : {(result["amount"]):,}원")
    total += result["amount"]
print(f"총 결제 금액 : {(total):,}원")










        
