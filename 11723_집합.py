## [1st try: set 자료형 활용, set 안의 요소는 string] >> 시간초과로 실패
# import sys
# input = sys.stdin.readline

# M = int(input())
# num_set = set()

# for i in range (M):
#     keyword = input().rstrip()
#     if keyword == 'all': 
#         num_set = set(str(i) for i in range(1, 21))
#     elif keyword == 'empty': 
#         num_set.clear()
#     else : 
#         op, x = keyword.split()
#         if op == 'add': 
#             num_set.add(x)
#         elif op == 'remove': 
#             num_set.discard(x)
#         elif op == 'check': 
#             print(1 if x in num_set else 0)
#         elif op == 'toggle': 
#             num_set.discard(x) if x in num_set else num_set.add(x)

## [2nd try: set 자료형 활용, set 안의 요소는 int] >> 성공
# import sys
# input = sys.stdin.readline

# M = int(input())
# num_set = set()

# for i in range (M):
#     keyword = input().rstrip()
#     if keyword == 'all': 
#         num_set = set(i for i in range(1, 21))
#     elif keyword == 'empty': 
#         num_set.clear()
#     else : 
#         op, x = keyword.split()
#         x = int(x)
#         if op == 'add': 
#             num_set.add(x)
#         elif op == 'remove': 
#             num_set.discard(x)
#         elif op == 'check': 
#             print(1 if x in num_set else 0)
#         elif op == 'toggle': 
#             num_set.discard(x) if x in num_set else num_set.add(x)

## [3rd try: 비트마스킹 활용] >> 성공
import sys
input = sys.stdin.readline

M = int(input())
s = 0b0

for i in range (M):
    op, *x_lst = input().rstrip().split()
    if op == 'all': 
        s = ~(0b0)
    elif op == 'empty': 
        s = 0b0
    else : 
        x = 0b1 << int(x_lst[0])
        if op == 'add': 
            s = s | x
        elif op == 'remove': 
            s = s & ~x
        elif op == 'check': 
            print (1 if s & x == x else 0)
        elif op == 'toggle': 
            s = s ^ x