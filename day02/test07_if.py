# date : 20240130
# desc : if문 응용
import datetime

now = datetime.datetime.now() # 현재의 년월일 시분초 가져옴

if now.hour < 12:
    print('오전입니다.')
else: # if now.hour >= 12:
    print('오후입니다.')