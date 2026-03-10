
checkList = ["DB 마이그레이션 완료 여부","application-prod.properties 설정 확인","JWT Secret Key 변경 여부","CORS 허용 도메인 설정 완료","API 엔드포인트 테스트 통과"]
noList =[]
cnt = 1
for i in checkList:
    answer = input(f"[{cnt}/5] {i} Y/N : ").upper()
    cnt += 1
    if answer == "Y":
        print("→ 완료")
    elif answer == "N":
        print("→ 미완료")
        noList.append(i)
    else:
        print("입력값이 올바르지 않습니다.")
if len(noList) == 0:
    print("배포 승인! 배포를 진행하세요.")
else:
    print("배포 보류! N개 항목을 해결 후 재시도하세요.")
    for i in noList:
        print(f"· {i}")
    
        