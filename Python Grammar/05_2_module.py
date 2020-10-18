import mod1
import mod2

# from mod1 import add : mod1 모듈에서 add 함수를 사용할 수 있게 한다.
# from mod1 import add, sub / from mod1 import *: add, sub 함수 모두 사용할 수 있게 한다.


print(mod1.add(3, 4))
print(mod1.sub(4, 2))

print(mod2.PI)  # 모듈의 변수 사용가능
a = mod2.Math()  # 모듈의 클래스 사용가능
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))
