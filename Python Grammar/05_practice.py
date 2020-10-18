# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)


# # Q2
# class MaxLimitCalculator(Calculator):


# Q4
list1 = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x: x > 0, list1)))


# Q5
print(int('0xea', 16))


# Q6
list2 = [1, 2, 3, 4]
print(list(map(lambda x: x * 3, list2)))


# Q7
list3 = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(list3) + min(list3))


# Q8
print(round(17 / 3, 4))


# Q9
