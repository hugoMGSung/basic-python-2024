# file: test17_input.py
# desc: 콘솔 입력

# 출력- 컴퓨터화면, 프린터, 스피커, 빔프로젝터, VR, ...
# 입력- 콘솔입력(키보드), 마우스입력, 목소리, 조이스틱, 터치스크린
# input('내용추가') 반드시!
temp_val = input('곱할 수(정수) 입력 > ')
if temp_val.isnumeric() == True: # 숫자입력이 아니면 튕겨내기
    temp_val = int(temp_val) # 문자열형에서 정수형로 변환(형변환)
    print(f'입력값 = {temp_val}')
    # 곱하기
    result = temp_val * 5
    print(f'결과 = {result}')
else:
    print('잘못된 입력, 정수만 입력하세요.')


