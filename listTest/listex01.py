products = ['노트북', '마우스', '키보드', '모니터', '웹캠']
stocks = [15, 3, 8, 22, 5]
total = 0
print("===재고현황===")
for i in range(0,len(products)):
    if stocks[i] < 10:
        print(f"{products[i]} {stocks[i]}개 재고부족")
    else:
        print(f"{products[i]} {stocks[i]}개")
    total += stocks[i]
print()
print(f"전체 재고 합계 : {total}개")

    #f-string 사용하면 해결이지만
    # 파이썬은 문자와 숫자를 하나로 나열할 수 없다.
    # 그러므로 str()함수를 이용해 숫자를 문자열로 변환하여 나열한다.
