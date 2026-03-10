pwlen = "X"
pwNum = "X"
pwUpper = "X"
pwLow = "X"
pwSpe = "X"
cnt = 0
while True:
    pw = input("비밀번호를 입력하세요 : ")
    isSpe = len(pw)
    if len(pw) >= 8:
        pwlen = "Ο"
        cnt +=1
    for ch in pw:
        if ch >= '0' and ch <= '9':
            pwNum = "Ο"
            cnt +=1
            isSpe= isSpe -1
        if ch >= 'A' and ch <= 'Z':
            pwUpper = "Ο"
            cnt +=1
            isSpe= isSpe -1
        if ch >= 'a' and ch <= 'z':
            pwLow = "Ο"
            cnt +=1
            isSpe= isSpe -1
    if isSpe > 0:
            pwSpe = "Ο"
            cnt +=1
    print(f"{cnt}")
    print(f"[{pwlen}]길이 8자 이상")
    print(f"[{pwNum}]숫자 포함여부")
    print(f"[{pwUpper}]대문자 포함여부")
    print(f"[{pwLow}]소문자 포함여부")
    print(f"[{pwSpe}]특수문자 포함여부")
    if pwlen=="Ο" and pwNum=="Ο" and pwUpper=="Ο" and pwLow=="Ο" and pwSpe=="Ο":
        print("비밀번호 강도 : 매우강함")
    else:
        print("비밀번호 강도 : 취약")
    break


    
