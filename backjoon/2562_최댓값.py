
import sys
input = sys.stdin.readline

## 1st try: 순회하면서 이전 숫자보다 큰 숫자일 경우 최댓값과 최댓값 인덱스를 갱신
# max = 0
# max_idx = 0
# for idx in range (1, 10):
#     num = int(input())
#     if num > max : 
#         max = num
#         max_idx = idx
# print(max)
# print(max_idx)

## 2nd try: 리스트의 max, index 함수 활용
num_lst = []
for i in range (9):
    num_lst.append(int(input()))

print(max(num_lst))
print(num_lst.index(max(num_lst))+1)