from collections import Counter
dicti = [
    {"subject":"Python 프로그래밍","score":92,"credit":3},
    {"subject":"SpringBoot 개발        ","score":88,"credit":3},
    {"subject":"React 프론트엔드","score":76,"credit":2},
    {"subject":"데이터베이스       ","score":95,"credit":3},
    {"subject":"알고리즘           ","score":68,"credit":2},
]
totalcredit = 0
totalavgpoint= 0
spread = []
print(f"{"=========성적표==========":^72}")
print()
print(f"과목                  점수           학점        학점포인트        이수학점")
print("-"*75)
for oneList in dicti:
    if oneList["score"] < 60:
        grade = "F"
        point = 0
        spread.append("F")
    elif oneList["score"] < 70:
        grade ="D"
        point = 1.0
        spread.append("D")
    elif oneList["score"] < 75:
        grade ="C"
        point = 2.0
        spread.append("C")
    elif oneList["score"] < 80:
        grade ="C+"
        point = 2.5
        spread.append("C+")
    elif oneList["score"] < 85:
        grade ="B"
        point = 3.0
        spread.append("B")
    elif oneList["score"] < 90:
        grade ="B+"
        point = 3.5
        spread.append("B+")
    elif oneList["score"] < 95:
        grade ="A"
        point = 4.0
        spread.append("A")
    else:
        grade ="A+"
        point = 4.5
        spread.append("A+")
    spread.sort()
    totalcredit += oneList["credit"]
    avgpoint = point*oneList["credit"]
    totalavgpoint += avgpoint
    print(f"{oneList["subject"]}\t{oneList["score"]}\t\t{grade}\t\t{point}\t\t{oneList["credit"]}")
    print()
print(f"GPA : {(totalavgpoint/totalcredit):.2f} / 4.50 총 ({totalcredit})학점")
ct = Counter(spread)
d = dict(ct)
print(f"학점 분포 : {d}")


#gradeCount = []
# for cour in courses:
#   grade = cour["grade"]
# 이미 학점이 존재하면 +1, 아니면 1
# if grade in gradeCount:
#   gradeCount[grade] +=1
# else:
#   gradeCount[grade] = 1