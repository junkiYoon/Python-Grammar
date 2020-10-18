a = input()  # input 사용자 입력, 입력되는 모든 것을 문자열로 취급
print(a)

number = input("숫자를 입력하세요: ")
print(f"입력한 숫자는 {number}.")

print("life""is""too short")  # ""로 둘러싸인 문자열은 + 연산과 동일
print("life", "is", "too short")  # 문자열 띄어쓰기는 콤마로 한다
for i in range(10):
    print(i, end=' ')  # 한 줄에 결과값 출력하려면 매개변수 end 를 사용해 끝 문자 지정
