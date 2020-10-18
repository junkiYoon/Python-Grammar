def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if __name__ == "__main__":  # import 하자마자 실행되는 것 방지, 파일 실행 => 참, 대화형 인터프리터 모듈 부름 => 거짓
    print(add(1, 4))
    print(sub(4, 2))
# __name__ : 직접 파일 실행 => __name__ = __main__ / 파이썬 셸, import 할 경우 => __name__ = mod1(모듈 이름 값)
