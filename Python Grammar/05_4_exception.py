try:
    4 / 0
except ZeroDivisionError as e:  # except 발생오류 as 오류 메시지 변수
    print(e)
finally:
    print('예외 발생 여부와 상관없이 수행')

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')  # pass : 오류 회피
except IndexError:
    print('인덱싱 할 수 없습니다.')
# except ZeroDivisionError as e:
#    print(e)
# except IndexError as e:
#    print(e)
# 같다
# except (ZeroDivisionError, IndexError) as e:
#    print(e)


class Bird:
    def fly(self):
        raise NotImplementedError  # raise : 오류 발생 시키기

