# 딕셔너리 = 오브젝트이다
# 딕셔너리 => key : value 가 쌍으로 존재한다.
# 딕셔너리 추력하는 방법
#   dict['key']   절대 dict.key 로 출력할 수 없다.
# phone_book = {'name':'홍길동','age':7,'class':'고급'}
phone_book = {}
phone_book['홍길동'] = '010-1234-1234'
phone_book['강감찬'] = '010-4321-1234'
phone_book['이순신'] = '010-1233-1994'

print(phone_book)
# {'홍길동': '010-1234-1234', '강감찬': '010-4321-1234', '이순신': '010-1233-1994'}

#모든 키만 출력하고싶을때
print(phone_book.keys())
#dict_keys(['홍길동', '강감찬', '이순신'])

#모든 값만 출력하고싶을때
print(phone_book.values())
#dict_values(['010-1234-1234', '010-4321-1234', '010-1233-1994'])

# 문제 phone_book을  강감찬 010-4321-1234  형식으로 출력해라
# 단 ,for문을 사용해서
print("=========")
for line in phone_book:
    print(line,phone_book[line])

