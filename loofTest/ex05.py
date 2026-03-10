
cnt = 0
total = 0
criticalCnt = 0

text = int(input("측정 횟수를 입력하세요 : "))
for i in range(text):
    ms = int(input("응답 시간을 입력하세요(ms) : "))
    print(f"응답시간{i+1} (ms) : {ms}")
    if ms > max:
        max = ms
    if i == 0:
        min = ms
    if ms < min:
        min = ms
    total = total + ms
    if ms <= 100:
        print("FAST")
        cnt+=1
    elif ms > 100 and ms <= 300:
        print("NORMAL")
        cnt+=1
    elif ms > 300 and ms <= 1000:
        print("NORMAL")
        cnt+=1
    else:
        print("CRITICAL")
        cnt+=1
        criticalCnt+=1


print(f"평균 응답 시간 : {(total/cnt):.1f}")
print(f"최대  : {max} |  최소 : {min}")
if criticalCnt/cnt >= 0.1:
    print("SLA 위반! 서버 점검이 필요합니다.")

    