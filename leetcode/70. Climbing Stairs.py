class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. 실패 - 시간 초과 (이렇게 하면 O(2^n))
        # def test(n):
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2
        #     else:
        #         return test(n-1) + test(n-2)
        # return test(n)

        # 2. 성공
        # memo = [0]*46
        # memo[1] = 1
        # memo[2] = 2
        
        # def stairs_dp(n):
        #     if memo[n] != 0:
        #         return memo[n]
        #     memo[n] = stairs_dp(n-2) + stairs_dp(n-1)
        #     return memo[n]

        # return stairs_dp(n)

        # 3. 성공
        def stairs_dp(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            
            prev2 = 1
            prev1 = 2

            for i in range (3, n+1):
                cur = prev2 + prev1
                prev2 = prev1
                prev1 = cur

            return (cur)

        return stairs_dp(n)