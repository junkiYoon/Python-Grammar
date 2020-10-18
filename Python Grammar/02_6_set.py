# -*- coding: utf-8 -*-

# set, 중복을 허용하지 않는다, 순서가 없다
s1 = set([1, 2, 3])
print(s1)
s2 = set("Hello")
print(s2)

# set 자료형에 저장된 값을 인덱싱으로 접근 => 리스트나 튜플로 변환 후 접근
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])
t1 = tuple(s1)
print(t1)
print(t1[0])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)  # 교집합
print(s1.intersection(s2))  # == s2.intersection(s1)
print(s1 | s2)  # 합집합
print(s1.union(s2))  # == s2.union(s1)
print(s1 - s2)  # 차집합
print(s1.difference(s2))

s1 = set([1, 2, 3])
s1.add(4)  # 값 1개 추가
print(s1)
s1.remove(4)  # 특정 값 제거
print(s1)
s1.update([4, 5, 6])
print(s1)