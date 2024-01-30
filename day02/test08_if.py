# desc : 홀수/짝수 또는 배수
number = int(input('정수입력 > ')) # 입력받은 후 정수로 변경

if number % 5 == 0: # 짝수 또는 배수
    print('5의 배수')
else: # 홀수 또는 나머지
    print('5의 배수가 아님')