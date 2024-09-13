## [case 1: 정규식 활용] > 시간초과
# import sys
# input = sys.stdin.readline

# N = int(input())

# def cal(x):
#     if x in (1, 2, 3): return 1
#     elif (x%3 == 0 and x%2 == 0):
#       return min(cal(x//3),cal(x//2), cal(x-1))+1
#     elif (x%3 == 0):
#       return min(cal(x//3),cal(x-1)) + 1
#     elif (x%2 == 0):
#       return min(cal(x//2),cal(x-1)) + 1
#     else:
#       return cal(x-1)+1

# for n in n_lst:
#   print(n)

import sys
input = sys.stdin.readline

N = int(input())
n_lst = [0] * (10**6+1)


for i in range (2, N+1):
    n_lst[i] = n_lst[i-1] + 1
    if (i%2==0):
        n_lst[i] = min(n_lst[i//2]+1, n_lst[i])
    if (i%3==0):
        n_lst[i] = min(n_lst[i//3]+1, n_lst[i])
    
print(n_lst[N])