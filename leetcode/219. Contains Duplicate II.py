class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 실패 - time limit exceeded 
        # for i in range (len(nums)):
        #     for j in range(1, k+1):
        #         if i + j < len(nums):
        #             if nums[i] == nums[i+j]:
        #                 return (True)
                
        # return (False)

        # 성공
        num_dict = {}
        for i in range (len(nums)):
            if nums[i] in num_dict:
                if abs(num_dict[nums[i]] - i) <= k:
                    return (True)
            num_dict[nums[i]] = i

        return (False)