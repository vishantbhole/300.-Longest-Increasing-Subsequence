# 300. Longest Increasing Subsequence

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) - 1 , -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i] , 1 + res[j])
        return max(res)

if __name__ == "__main__":
    sol = Solution()
    s = [10,9,2,5,3,7,101,18]
    print("Output is : ", sol.lengthOfLIS(s))
