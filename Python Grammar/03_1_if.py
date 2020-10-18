# -*- coding: utf-8 -*-

print(1 in [1, 2, 3])  # x in 리스트/튜플/문자열 : 리스트/튜플/문자열 안에 x가 있으면 true
print(1 not in [1, 2, 3])  # x not in 리스트/튜플/문자열 : 리스트/튜플/문자열 안에 x가 없으면 true
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("Take taxi")  # 아무 동작 하지 않을 때 => pass
else:
    print("Walk")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("Take taxi")
elif card:  # c언어에서 else if == Python에서 elif
    print("Take taxi")
else:
    print("Walk")

# 수행할 문장이 한 줄일때
# if 'money' in pocket: pass
# else: print("카드를 꺼내라")

score = 88
message = "success" if score >= 60 else "failure"
# if score >= 60:
#   message = "success"
# else:
#   message = "failure"
print(message)