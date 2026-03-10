selCnt =0
insCnt =0
delCnt =0
updCnt =0
total=0
while True:
    text = input("쿼리 유형 입력 : ").upper()
    if text =="SELECT":
        selCnt += 1
        total += 1
    elif text == "INSERT":
        insCnt +=1
        total += 1
    elif text == "DELETE":
        delCnt += 1
        total += 1
    elif text == "UPDATE":
        updCnt +=1
        total +=1
    elif text == "REPORT":
        print("중간 쿼리 실행 현황 REPORT")
        print(f"SELECT : {selCnt}회")
        print(f"INSERT : {insCnt}회")
        print(f"UPDATE : {updCnt}회")
        print(f"DELETE : {delCnt}회")
        print(f"TOTAL : {total}회")
    elif text == "EXIT":
        print("최종 쿼리 실행 현황")
        print(f"SELECT : {selCnt}회")
        print(f"INSERT : {insCnt}회")
        print(f"UPDATE : {updCnt}회")
        print(f"DELETE : {delCnt}회")
        print(f"TOTAL : {total}회")
        if total/selCnt >= 0.7:
            print("SELECT가 전체의 70% 이상이면 'SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")
        break
    else:
        print("올바른 쿼리 실행 부탁드립니다.")