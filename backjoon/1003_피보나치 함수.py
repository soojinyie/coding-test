import sys
input = sys.stdin.readline

def f(n):
    if (n==0):
        f_lst[0] = 0
        return 0
    elif (n==1):
        f_lst[1] = 1
        return 1
    
    if f_lst[n] != 0: 
        return f_lst[n]
    else :
        f_lst[n] = f(n-1) + f(n-2)
        return f_lst[n]

T = int(input())
for _ in range (T):
    n = int(input())
    f_lst = [0]*41
    f(n)
    if (n==0):
        print(1, 0)
    elif (n==1):
        print(0, 1)
    else:
        print(f_lst[n-1], f_lst[n])


