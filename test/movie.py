ticket_no,cinema,floor,movie ="2026-0309-01", "7관","4층", "파이썬의 습격"
startTime,endTime = "14:30","16:10"
adultPrice,q1,kidPrice,q2 = 15000,2,10000,1
amt1,amt2 = adultPrice*q1,kidPrice*q2
total= amt1+amt2
line1,line2 = "="*60,"-"*60

print(f"{line1}\n{"PYTHON CINEMA":^62}\n{line1}")
print(f"{"티켓번호 :"} {ticket_no}")
print(f"{"상영관 :"} {cinema} ({floor})")
print(f"{"영화명 :"} {movie}")
print(f"{"상영시간 :"} {startTime}~{endTime}\n{line2}")
print(f"{"구분":<22}{"단가":<10}{"인원":<10}{"금액":<5}\n{line2}")
print(f"{"일반 성인":<20}{adultPrice:<12,}{q1:<12}{amt1:<5,}")
print(f"{"청소년":<21}{kidPrice:<12,}{q2:<12}{amt2:<5,}\n{line2}")
print(f"{"총 결제 금액":<42} {total:<5,}\n{line1}")