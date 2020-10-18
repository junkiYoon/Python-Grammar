# -*- coding: utf-8 -*-
a = "Life is too short, You need Python"
print(a[0:4])  # a[0:4] == a[0] + a[1] + a[2] + a[3]
print(a[12:17])
print(a[19:])  # a[19:] == a[19:33]
print(a[:17])  # a[:17] == a[0:17]
print(a[:])  # a[:] == a
print(a[19:-7])

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

a = "Pithon"
print(a[:1] + 'y' + a[2:])  # 문자열 요소 바꾸기 ( a[1] = 'y' => X )

# 문자열 포매팅 %d : 숫자, %s : 문자열, % (숫자, 문자열, 변수)
print("I eat %d apples." % 3)  # 숫자 대입
print("I eat %s apples." % "five")  # 문자열 대입
number = 3
print("I eat %d apples." % number)  # 숫자 들어있는 변수 대입
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))  # 2개 이상의 값 대입 => %(변수, 변수, ...)
'''
포맷 코드
%s : 문자열
%c : 문자 1개
%d : 정수
%f : 부동소수
%o : 8진수
%x : 16진수
%% : 문자 % 자체
'''