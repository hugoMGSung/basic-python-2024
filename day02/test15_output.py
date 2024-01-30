# file: test15_output.py
# desc: 콘솔출력 포맷양식 String Format

string_1 = '{}'.format(10) # {}위치에 함수 뒤에 들어있는 값을 치환, 원하는 양식으로 표현
print(type(string_1))

name = '성명건' #input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000, '만', '빌려주세요')
print(string_3)
#정수를 문자열포맷 d
#=: 기호와 숫자를 분리 , 02d: 두자리수 만들때 빈자리 0으로 채우기
string_4 = '_____{:=+010d}_____'.format(-100) # 
print(string_4)
#실수 문자열포맷 f (기본 소수점6자리)
#7.2f 전체 자리수를 7자리로, 소수점 뒤는 2자리 fix
val = 78.3333333333333
string_5 = '_____{:7.2f}_____'.format(val)
print(string_5)

# 파이썬 3.6 이후 도입. format() 함수를 아예 사용안함
string_6 = f'_____{val:7.2f}_____'
print(string_6)

string_7 = 'Hello, World!'
print(string_7.upper()) # upper case 대문자변환
print(string_7.lower()) # 모두 소문자로
print(string_7.lower().capitalize())

print(string_7.split(',')) # 특정한 단어로 자르는 함수

string_8 = 'Hello, I am MG Sung. I am a lecturer. Good Luck for your day.' 
words = string_8.split(' ')
print(words)
print(f'문장의 단어 갯수는 {len(words)}개입니다.')

string_9 = 'A10'
print(string_9.isalnum()) # True
print(string_9.isnumeric()) # False A 알파벳
string_10 = '10.5' # 소수점은 함수를 만들어서 처리해야...
print(string_10.isdecimal()) # False

print('안냥' in '안녕하세요') # 문장안에 단어가 있는지 확인