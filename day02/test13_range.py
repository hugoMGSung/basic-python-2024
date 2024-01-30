# file: test13_range.py
# desc: 리스트 범위지정

list_a = [1,2,3,4,5,6,7,8,9,10]
print(list_a)

# 범위 지정 range(n), 0부터 n개의 범위 수를 생성
print(list(range(5)))
print(list(range(1, 6))) # 1~5
print(list(range(2, 21, 2))) # 2부터 20(+1)까지 2씩 증가
print(list(range(1, 20, 2))) # 1부터 19까지 2씩 증가
print(list(range(10, -1, -1))) # countdown

list_a = list(range(1, 101)) # range() 클래스
print(list_a)

list_a = [i for i in range(1, 101)] # 리스트 컨프리헨션
print(list_a)

