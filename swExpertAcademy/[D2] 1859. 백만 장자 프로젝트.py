import sys
input = sys.stdin.readline

T = int(input())
answer = []
for tc in range (T):
    N = int(input())
    p_lst = list(map(int, input().split()))
    max_price = p_lst[N-1]
    sum_profit = 0
    for i in range (N-1, -1, -1):
        if p_lst[i] > max_price: 
            max_price = p_lst[i]
        sum_profit += max_price - p_lst[i]
    
    print(f'#{tc+1} {sum_profit}')

