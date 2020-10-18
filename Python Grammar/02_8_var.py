# -*- coding: utf-8 -*-

a = [1, 2, 3]
b = a
print(id(a))  # a의 주소
print(id(b))  # a 와 b 의 주소가 같음
a[1] = 4  # 그래서 a 를 바꾸면
print(a)
print(b)  # b 도 바뀜

# 리스트 복사하기
b = a[:]  # : 이용
a[1] = 4
print(a)
print(b)
from copy import copy
c = copy(a)  # copy 모듈 이용
print(b is a)

a, b = ('python', 'life')  # 튜플로 변수 만들기
print(a)
print(b)
[a, b] = ['python', 'life']  # 리스트로 변수 만들기
print(a)
print(b)
a = b = 'python'  # 여러 개의 변수에 같은 값 대입
print(a)
print(b)
a = 3
b = 5
a, b = b, a
print(a)
print(b)