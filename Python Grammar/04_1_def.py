def add(a, b):
    return a+b


result = add(b=5, a=3)  # 매개변수 지정 가능
print(result)


def add_many(*args):  # 매개변수 이름 앞에 *를 붙이면 입력값을 모두 모아 튜플로 만든다
    result = 0
    for i in args:
        result += i
    return result


result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)


def print_kwargs(**kwargs):  # 매개변수 앞에 **를 붙이면 입력값을 딕셔너리로 만들어 저장
    print(kwargs)


print_kwargs(name='foo', age=3)


def add_and_mul(a, b):
    return a+b, a*b  # 함수의 결괏값은 하나이기 때문에 튜플값으로 리턴
# return 을 2개 쓰면 위에 쓴 값만 리턴
# return 을 사용해서 함수를 빠져나갈 수 있다


result = add_and_mul(3, 4)
print(result)


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


print(say_myself("윤준기", 17))  # == say_myself("윤준기", 17, True)


add2 = lambda a, b: a+b  # lambda 매개변수: 표현식
result = add2(3, 4)
print(result)
