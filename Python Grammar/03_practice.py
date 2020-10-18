# -*- coding: utf-8 -*-

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
# shirt

height = 5
star = 0
while star <= height:
    print("*" * star)
    star = star + 1

'''
number = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
'''
number = [1, 2, 3, 4, 5]
result = [i * 2 for i in number if i % 2 == 1]
print(result)
