zerocnt = 0
cnt = 0

token = int(input("토큰 수를 입력하세요 : "))
for i in range(0,token):
    time = int(input("잔여시간(분) : "))
    if time <= 0:
        print("[만료]즉시 재발급 필요")
        zerocnt+=1
    elif time >= 1 and time <= 10:
        print("[위험]곧 만료됩니다. 갱신권장")
        zerocnt+=1
    elif time >= 11 and time <= 30:
        print("[주의]만료가 가까워지고있습니다.")
        zerocnt+=1
    elif time >= 31:
        print("[정상]유효한 토큰")
        cnt+=1
print("==요약==")
print(f"정상 토큰: {cnt}개 / 위험,주의,만료토큰 {zerocnt}개")