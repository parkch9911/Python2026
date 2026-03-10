# 다중 for문을 이용해서 구구단 2단부터 9단까지 출력
# 증감값은 생략해도 기본값으로 +1 이다.
for i in range(2,10):
    for j in range(2,10):
        print(f"{i}x{j}={i*j}")