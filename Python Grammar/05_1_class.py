class FourCal:
    def __init__(self, first, second):  # __init__ : 생성자, 객체가 생성되면 자동으로 호출
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal(4, 2)  # 클래스 생성
b = FourCal(3, 8)
print(a.add())
print(b.add())


class MoreFourCal(FourCal):  # 클래스 상속 : FourCal 의 모든 기능 사용 가능(기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황)
    def pow(self):
        result = self.first ** self.second
        return result


c = MoreFourCal(4, 2)
print(c.pow())


class SafeFourCal(FourCal):
    def div(self):  # 메서드 오버라이딩 : div 메서드 덮어쓰기
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


d = SafeFourCal(4, 0)
print(d.div())


class Family:
    lastname = '김'


f1 = Family()
f2 = Family()
print(f1.lastname)
print(f2.lastname)
Family.lastname = '박'
print(f1.lastname)
print(f2.lastname)