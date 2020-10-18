# -*- coding: utf-8 -*-

test_list = ['one', 'two', 'three']
for i in test_list:  # 첫 번째 요소부터 i 변수에 대입
    print(i)         # i 출력

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:  # 튜플 자료형이기 때문에 자동으로 변수에 대입
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("No.%d student is passed." % number)
    else:
        print("No.%d student is failde." % number)

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("No.%d student is passed, congratulations." % number)

a = range(1, 10)  # 0부터 10미만의 숫자를 포함하는 range 객체 생성
print(a)
a = range(1, 11)  # 1부터 11미만

add = 0
for i in range(1, 11):
    add = add + i
print(add)

number = 0
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("No.%d student is passed, congratulations." % (number+1))

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)  # a 리스트의 각 항복에 3을 곱한 결과를 result 리스트에 담음
print(result)
# 리스트 내포 이용
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)
result = [num * 3 for num in a if num % 2 == 0]  # 짝수만 담음
print(result)