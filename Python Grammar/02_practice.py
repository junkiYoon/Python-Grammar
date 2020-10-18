# -*- coding: utf-8 -*-

# Q1
print((80 + 75 + 55) / 3)

# Q2
print(13 % 2)

# Q3
pin = '881120-1068234'
print(pin[:5] + ' ' + pin[7:])

# Q4
print(pin[7])

# Q5
a = "a:b:c:d"
print(a.replace(':', '#'))

# Q6
num_list = [1, 3, 5, 4, 2]
num_list.sort()
num_list.reverse()
print(num_list)

# Q7
l_life = ['Life', 'is', 'too', 'short']
s_life = ' '.join(l_life)
print(s_life)

# Q8
t_num = (1, 2, 3)
four = (4,)
print(t_num + four)

# Q10
a = {'A': 90, 'B': 80, 'C': 70}
print(a.pop('B'))

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s_a = set(a)
print(s_a)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)  # [1, 4, 3]
