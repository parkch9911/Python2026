response = {
'code' : 200,
'message': 'success',
'data' 
: [
{'userId': 'user01', 'name': '이자바', 'score': 95},
{'userId': 'user02', 'name': '박리액트', 'score': 82},
{'userId': 'user03', 'name': '최스프링', 'score': 91},
{'userId': 'user04', 'name': '정마이바티스', 'score': 78},
]
}
cnt = 0
good = []

print("===전체성적===")
for user in response["data"]:
    print(f"{user["name"]} ({user["userId"]}): {user["score"]}점")
    if user["score"] >= 90:
        cnt+= 1
        good.append(user)
print(f"===우수 수강생 (90점 이상) {cnt}명===")
for gooduser in good:
    print(f"★  {gooduser["name"]}  {gooduser["score"]}점")

    