# file: test20_function.py
# desc: 함수 만들기(계산기 기능)

def 더하기(첫번째, 두번째) -> int:
    계산값 = 첫번째 + 두번째  
    return 계산값

def minus(x, y) -> int:
    result = x - y
    return result

def multi(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> float:
    result = x / y
    return result

def say_hello() -> None:
    print('Hello')
    # return None 은 생략

say_hello()
print('더하기 -> ')
a, b = map(int, input('두 정수 입력 > ').split(' '))
결과 = 더하기(a, b)  # 리턴은 함수 결과값으로 바뀐다!
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a, b)}')
print(f'{a} x {b} = {multi(a, b)}')
print(f'{a} ÷ {b} = {divide(a, b)}')



