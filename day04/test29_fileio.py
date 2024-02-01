# file: test29_fileio.py
# desc: 텍스트 파일 읽기

f = open('sample.txt', mode='r', encoding='utf-8')
# 아래의 방법은 기초적이나 용량문제로 큰파일은 읽기 불가
# text = f.read() # 텍스트파일 모든 텍스를 전부 한번에 읽어온다. 
# print(text)
# 아래는 가장 일반적..
while True:
    line = f.readline()
    if not line: break  # 조건문, 반복문 내의 코드가 한줄만 있으면 if 옆에 적을 수 있음

    print(line.replace('\n', ''))

f.close()