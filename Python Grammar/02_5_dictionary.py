# -*- coding: utf-8 -*-

# 딕셔너리 기본모습
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

# 주의
a = {1: 'a', 1: 'b'}  # Key 가 중복되면 하나를 제외한 나머지가 무시됨
print(a)
# a = {[1, 2]: 'hi'} => 오류  Key 에 리스트 사용 불가

print(dic.keys())  # Key 리스트 만들기
print(dic.values())  # Value 리스트 만들기
print(dic.items())  # Key, Value 쌍 얻기
dic.clear()  # Key: Value 쌍 모두 지우기
print(dic)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
get = a.get('name')  # Key 로 value 얻기, 존재하지 않는 키로 가져오려는 경우 None 을 돌려줌
print(get)
# 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 가져오게 할 수 있다.
# a.get('foo', 'bar') => foo  가 없기 때문에 bar 출력
print('name' in a)  # 해당 Key 가 딕셔너리 안에 있는지 조사
print('email' in a)  # 존재하면 Ture, 존재하지 않으면 False 출력
