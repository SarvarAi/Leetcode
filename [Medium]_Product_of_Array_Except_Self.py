from typing import List, Dict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



if __name__ == '__main__':
    test_list_1 = [1,2,3,4]
    test_list_2 = [-1,1,0,-3,3]

    sol = Solution()
    answer = sol.productExceptSelf(nums=test_list_1)
    print(answer)