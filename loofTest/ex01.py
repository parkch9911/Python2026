HTTPstatus = int(input("HTTP 상태코드를 입력하세요 : "))
status =""
comment = ""
if HTTPstatus//100 == 2:
    comment = "2xx(성공)"
    if HTTPstatus%200 == 0:
        status = "200: OK - 요청 성공"
    elif HTTPstatus%200 == 1:
        status = "201: Created - 리소스 생성 성공"
    else:
        status="Unknown Status Code"
        comment = "올바른 값을 입력해주세요"
elif HTTPstatus//100 == 4:
    comment = "4xx(클라이언트 오류)"
    if HTTPstatus%400 == 0:
        status="400: Bad Request - 잘못된 요청"
    elif HTTPstatus%400 == 1:
        status="401: Unauthorized - 인증 필요"
    elif HTTPstatus%400 == 3:
        status="403: Forbidden - 접근 권한 없음"
    elif HTTPstatus%400 == 4:
        status="404: Not Found - 리소스 없음"
    else:
        status="Unknown Status Code"
        comment = "올바른 값을 입력해주세요"
elif HTTPstatus//100 == 5:
    comment = "5xx(서버 오류)"
    if HTTPstatus%500 == 0:
        status="500: Internal Server Error - 서버 내부 오류"
    else:
        status="Unknown Status Code"
        comment = "올바른 값을 입력해주세요"
else:
    status="Unknown Status Code"
    comment = "올바른 값을 입력해주세요"
print(f"{status}")
print(f"{comment}")
