import sys
input = sys.stdin.readline

price = int(input())

coin_lst = [500, 100, 50, 10, 5, 1]
total_coin_num = 0
to_change = 1000 - price 

for coin in coin_lst:
    coin_num = to_change//coin
    to_change = to_change%coin
    total_coin_num += coin_num

print(total_coin_num)