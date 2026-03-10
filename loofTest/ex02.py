digit = False
while True:
    userid = input("아이디를 입력하세요 : ")
    idlength = len(userid)
    if idlength > 12 or idlength < 3:
        print("아이디를 4자 이상 12자 이하로 입력해주세요")
    else:
        while True:
            # 이 밑이 비밀번호
            userpw = input("비밀번호를 입력하세요 : ")
            pwlength = len(userpw)
            for ch in userpw:
                if ch >= '0' and ch <= '9':
                    digit = True
            if pwlength < 8:
                print("비밀번호를 8자 이상 입력해주세요")
            #숫자 포함여부확인@@@@@@@@@
            elif digit == False:
                print("비밀번호에 숫자를 포함해주세요")
            else: #이 밑으론 이메일
                while True:
                    usermail = input("이메일을 입력하세요 : ")
                    if "@" not in usermail:
                        print("올바른 이메일 형식을 입력해주세요")
                    else:
                        print('유효성 검사 통과! API 요청을 전송합니다.')
                    break
            break
    break
print()
