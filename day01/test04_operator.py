# date : 20240129
# desc : 연산자

# 사칙연산 : + - *(곱하기) /(나누기) //(정수로 나누기) %(나눈 나머지), **(제승)
# 비교연산 : =(값 할당), ==(비교), >, <, >=, <=, !=(같지 않다)
# 논리연산 : and, or, not
print(2 * 10)
print(2 ** 10)

print(5 / 2) # 2.5 실수로 나누기
print(5 // 2) # 2 정수로 나누기
print(5 % 2) # 정수로 나누고 남은 나머지

print(5 == 4) # False
print(5 > 4) # True
print(5 >= 4) # True
print(5 <= 4) # False
print(5 < 4) # False
print(5 != 4) # True

print(5 <= 4 and (5/2 < 3)) # False and기준으로 왼쪽/오른쪽 모두 참이어야 참
print(5 <= 4 or (5/2 < 3)) # True
print(not (5 > 4)) # 참이면 거짓으로, 거짓이면 참으로 반대로
