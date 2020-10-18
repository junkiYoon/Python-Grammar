# -*- coding: utf-8 -*-

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("You hit tree %d times." % treeHit)
    if treeHit == 10:
        print("Tree is falling.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("You give me money, then I'll give you coffee.")
    coffee = coffee - 1
    print("Now, we have %d cups of coffee left" % coffee)
    if coffee == 0:
        print("Coffee was sold out. We are closed.")
        break

coffee = 10
while True:  # 무한루프
    money = int(input("Insert coin: "))
    if money == 300:
        print("I'll give you coffee.")
        coffee = coffee - 1
    elif money > 300:
        print("I'll give you coffee with %d change.")
        coffee = coffee - 1
    else:
        print("Return coin, and I won't give you coffee.")
        print("We have %d cups of coffee left." % coffee)
    if coffee == 0:
        print("Coffee was sold out. We are closed.")
        break

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue  # continue : while문의 맨 처음으로
    print(a)
