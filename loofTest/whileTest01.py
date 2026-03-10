# while 조건:
#       실행구문
# 파이썬은 break, continue 사용 가능
# 단 return은 함수에서만 사용 가능
# response = "아니"
# while response == "아니":
#     response = input("엄마, 밥 다 됐어?")

# print("먹자")

#break를 이용해서 수정
while True:
    res = input("밥 다 됐나요")
    if res != "아니":
        break
print("먹자")