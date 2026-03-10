# 문제) 1부터 50까지 합을 구하기
# 단, while문 이용

count =1
sum = 0
while count <= 50:
    sum+= count
    count +=1
print(sum)

# 다중 while문을 이용해서 구구단 2단부터 9단까지 출력
i=2
j=2
while i <= 9:
    while j <=9:
        print(f"{i}x{j}={i*j}")
        j = j + 1
    print()
    i+=1
    j=2
    

    
   
