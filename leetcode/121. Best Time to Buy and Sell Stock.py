# 오답 - 시간 초과
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range (len(prices)-1): # 순회하면서
            profit = - prices[i] + max(prices[i+1:]) # 지금 이후의 날들 중 가장 비싼 날에 팔았을 때의 수익
            if max_profit < profit: # 이번 수익이 지금까지의 최대 수익보다 크다면
                max_profit = profit # 최대 수익을 갱신

        return max_profit
    
# 정답
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for i in range (len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return profit