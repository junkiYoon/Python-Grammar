# -*- coding: utf-8 -*-
print("%10s" % "hi")  # %10s : 전체 길이가 10개인 문자열에서 대입되는 값을 오른쪽으로 정렬, 나머지는 공백
print("%-10sjane." % "hi")  # %-10s : hi를 왼쪽으로 정렬 나머지 공백
print("%0.4f" % 3.141592)
print("%10.4f" % 3.141592)

# format 함수
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
number = 3
print("I eat {0} apples".format(number))
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))  # format 함수로 2개 이상 값 넣기 {0}, {1}...
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))  # 이름으로 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))  # 인덱스와 이름 혼용
print("{0:<10}".format("hi"))  # 왼쪽 정렬
print("{0:>10}".format("hi"))  # 오른쪽 정렬
print("{0:^10}".format("hi"))  # 가운데 정렬
print("{0:=^10}".format("hi"))  # 공백 채우기
y = 3.141592
print("{0:0.4f}".format(y))  # 소수점 표현
print("{{ and }}".format())  # { 또는 } 표현

a = "Python is the best choice"
print(a.count('e'))  # 문자열 중 e의 개수
print(a.find('i'))  # 문자열 중 i가 처음 나온 위치, 찾는 문자나 문자열이 없을 시 -1
print(a.index('i'))  # 문자열 중 i가 처음 나온 위치, 찾는 문자나 문자열이 없을 시 오류
print(",".join('abcd'))  # abcd 문자열의 각각의 문자 사이에 , 삽입
print(a.upper())  # 소문자를 대문자로
print(a.lower())  # 대문자를 소문자로
a = ' hi '
print(a.lstrip())  # 왼쪽 공백 지우기
print(a.rstrip())  # 오른쪽 공백 지우기
print(a.strip())  # 양쪽 공백 지우기
a = "Life is too short"
print(a.replace("Life", "Your leg"))  # Life를 Your leg로 치환
print(a.split())  # 괄호 안에 아무 값도 없으면 공백 기준, 특정 값이 있으면 그 값을 구분자로