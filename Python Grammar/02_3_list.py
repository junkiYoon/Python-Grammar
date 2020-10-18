# -*- coding: utf-8 -*-

# 리스트, 리스트 안에는 어떠한 자료형도 포함 가능
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(b[0])  # b문자열의 0번째 값
print(b[0] + b[2])  # b문자열의 0번째 값과 2번째 값의 합
print(b[-1])

print(e[0])
print(e[-1])  # 마지막 요솟값인 리스트 출력
print(e[-1][0])  # 리스트에 포함된 리스트에서 요소 뽑아내기

print(b[0:1])  # 리스트 슬라이싱
print(b[:2])
print(b[1:])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # 리스트 더하기
print(a * 3)  # 리스트 반복
print(len(a))  # 리스트의 길이 구하기
print(str(a[2]) + "hi")  # str함수 : 정수나 실수를 문자열의 형태로 바꿔줌

a = [1, 2, 3]
a[2] = 4  # 리스트의 요솟값 수정
print(a)
del a[1]  # del함수 : 리스트 요소 삭제
print(a)
a = [1, 2, 3, 4, 5]
del a[2:]  # 슬라이싱 기법 사용
print(a)

a = [1, 2, 3]
a.append(4)  # 리스트에 요소 추가
print(a)
a = [1, 4, 3, 2]
a.sort()  # 리스트 정렬(문자 가능)
print(a)
a = ['a', 'c', 'b']
a.reverse()  # 리스트 뒤집기
print(a)
a = [1, 2, 3]
print(a.index(3))  # 3이 존재하는 위치, 존재하지 않으면 오류
a.insert(0, 4)  # insert(a, b) : 리스트의 a번째 위치에 b를 삽입
a = [1, 2, 3, 1, 2, 3]
a.remove(3)  # remove(x) : 리스트에서 첫 번째로 나오는 x를 삭제
print(a)
a = [1, 2, 3]
print(a.pop())  # 맨 마지막 요소 리턴 후 삭제
print(a)
a = [1, 2, 3, 1]
print(a.count(1))  # 리스트에 포함된 요소의 개수
a = [1, 2, 3]
a.extend([4, 5])  # 리스트에 리스트 추가
print(a)
b = [6, 7]
a.extend(b)
print(a)
