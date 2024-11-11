class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 첫 번째 풀이
        # if len(nums) != len(set(nums)):
        #     return (True)
        # else:
        #     return(False)

        # 두 번째 풀이
        num_set = set()
        for num in nums:
            if num in num_set: 
                return (True)
            num_set.add(num)
        return (False)