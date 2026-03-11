member = {'name' : '김파이썬','email' : 'python@example.com','age' : 28,'grade' : 'GOLD'}

print("===회원정보===")
for info in member:
    print(f"{info} : {member[info]}")
    if info == "age" and member[info] < 20:
        age = "주니어"
    elif info == "age" and member[info] >=20 and member[info] <40:
        age = "일반"
    elif info == "age" and member[info] >=40:
        age="시니어"
    if info != "phone":
        phone = "미등록"
print(f"연령구간: {age}")
print(f"전화번호: {phone}")
