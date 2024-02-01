# file: test30_fileio.py
# desc: 텍스트 파일 읽고 쓰기

fr = open('sample.txt', mode='r', encoding='utf-8')
fw = open('output.txt', mode='w', encoding='utf-8')

while True:
    line = fr.readline()
    if not line: break

    print('내용', line.replace('\n', ''))
    fw.write(line)

fr.close()
fw.close()