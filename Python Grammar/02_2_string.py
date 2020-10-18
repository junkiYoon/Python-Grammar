# -*- coding: utf-8 -*-
print('Hello World')  # 문자열 '' 또는 "" 로 묶기
food = "Python's favorite food is perl"  # 문자열에 '가 들어가면 ""로 묶기
# food = 'Python\'s favorite food is perl'
print(food)
say = '"Python is very easy." he says.'  # 문자열에 "가 들어가면 ''로 묶기
# say = "\"Python is very easy.\" he says."
print(say)

multiline1 = "Life is too short\nYou need python"  # \n : 줄바꿈
multiline2 = '''
Life is too short
You need python
'''                 # ''' ''' 또는 ''' '''로 묶기 : 줄 바꿈
print(multiline1)
print(multiline2)

head = "Python"
tail = " is fun!"
print(head + tail)  # 문자열 연결하기
print(head * 2)  # 문자열 반복

a = "Life is too short, You need Python"
print(len(a))  # len(a) : a의 문자열
print(a[0])  # 문자열 인덱싱
print(a[12])
print(a[-1])