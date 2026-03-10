dep = input("출발지를 입력하세요 : ")
arv = input("도착지를 입력하세요 : ")
km = float(input("이동거리를 입력하세요(km) : "))
time = int(input("탑승시간을 입력하세요(24시간) : "))
withKid = input("어린이 동반여부를 입력하세요 예/아니오 : ")
fee = 4800
addfee = (((km*1000)-2000)//100)*100

print("="*60)
print("택시요금안내")
print("="*60)
print(f"출발지 : {dep}")
print(f"도착지 : {arv}")
print(f"이동거리 : {km}km")
print(f"탑승시간 : {time}시")
print("="*60)

if withKid == "아니오":
    if time >= 22 or time <= 4:
        #할증 있을 때
        if km <= 2:
            print(f"기본요금 : 4800원")
            print(f"거리요금 : {0}원")
            print(f"심야할증 : {int((fee)//100)*20}원 (20%적용)")
            print(f"최종요금 : {int(fee+(fee/100)*20)}원")
            #할증있으면서 거리요금받을때
        else:
            print(f"기본요금 : 4800원")
            print(f"거리요금 : {addfee}원")
            print(f"심야할증 : {int((addfee+fee)//100)*20}원 (20%적용)")
            print(f"최종요금 : {int((addfee+fee)/100*20)+fee+addfee}원")
    else:
        #할증 없는거
        if km <= 2:
            print(f"기본요금 : {4800}원")
            print(f"거리요금 : {0}원")
            print(f"심야할증 : {0}원")
            print(f"최종요금 : {4800}원")
        else:
            print(f"기본요금 : 4800원")
            print(f"거리요금 : {int(addfee)}원")
            print(f"심야할증 : {0}원")
            print(f"최종요금 : {int(fee+addfee)}원")

elif withKid == "예": #애랑 탔을때 기본요금 = 0 거리요금만 계산함
    if time >= 22 or time <= 4:  #할증 붙을 때
        if km <= 2:
            print(f"기본요금 : {0}원")
            print(f"거리요금 : {0}원")
            print(f"심야할증 : {0}원")
            print(f"최종요금 : {0}원")
        else:
             # 거리요금만 내고 할증
            print(f"지불요금 : {int(((addfee)//10)*2+addfee)}원")
            print(f"기본요금 : {0}원")
            print(f"거리요금 : {addfee}원")
            print(f"심야할증 : {int((((addfee)//10)*2+addfee)-addfee)}원")
            print(f"최종요금 : {int(((addfee)//10)*2+addfee)}원")
    else: #할증 안 붙을 때
        if km <= 2:
            print(f"기본요금 : {0}원")
            print(f"거리요금 : {0}원")
            print(f"심야할증 : {0}원")
            print(f"최종요금 : {0}원")
        else:
            print(f"지불요금 : {int(addfee)}원")
            print(f"기본요금 : {0}원")
            print(f"거리요금 : {int(addfee)}원")
            print(f"심야할증 : {0}원")
            print(f"최종요금 : {int(addfee)}원")
            


