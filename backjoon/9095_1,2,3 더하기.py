import sys
# f(n) = f(n-1) + f(n-2) + f(n-3)

def cal(n):
    if(n==1):
        return 1
    elif (n==2):
        return 2
    elif (n==3):
        return 4
    else:
        return cal(n-1)+cal(n-2)+cal(n-3)