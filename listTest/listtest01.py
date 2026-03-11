# 리스트 = 배열과 같은 역할을 한다.
# 리스트 [숫자, 문자 , 혼합] 사용 가능하다.
# 동적 => 고정길이가 아니다.
# 다양한 편의 기능을 제공하다보니, 속도는 살짝 느리다.

heroes=[]
# 리스트 추가하는 방법
# append('추가할 문자')=> 맨 뒤에 추가
# insert(인덱스번호,'추가할 문자')=> 인덱스 번호에 추가
heroes.append("아이언맨")
heroes.append("닥터 스트레인지")
print(heroes)
heroes.insert(1,"왕과사는남자")
print(heroes)

# 리스트 삭제 : remove('삭제할 문자')
# del(인덱스번호)
# pop() => 배열의 맨 뒤 데이터 삭제
heroes.remove("왕과사는남자")
print(heroes)
del heroes[0]
print(heroes)
heroes.pop()
print(heroes)
print("========================")
heroes.append("a")
heroes.append("b")
heroes.append("c")
heroes.append("d")
print(heroes)

# for 문을 이용해서 출력하기
count = 1
for title in heroes:
    print(f"{count}.{title}")
    count+=1

for title in heroes:
    print(title,end=" ")
print("")
print("========================")
# 리스트 슬라이스 하기
# heroes[0:3] => 0번째부터 3개
# heroes[:3] => 처음부터 3개
# heroes[3:] => 3번째 부터 끝까지
cut = heroes[3:]
print(cut)

# 문제 ) movieTitle = []에 아래 영화 제목 4개를 추가하시오
print("========================")
movieTitle = []
movieTitle.append("아이언맨")
movieTitle.append("토르")
movieTitle.append("헐크")
movieTitle.append("스칼렛 위치")
for movie in movieTitle:
    print(movie,end=" ")
print("")

# 문제 ) movieTitle 에서 토르가 존재하면 삭제하고 출력
if "토르" in movieTitle:
    movieTitle.remove("토르")
print("================")
movieTitle.sort(reverse=True)
for movie in movieTitle:
    print(movie,end=" ")
print("")