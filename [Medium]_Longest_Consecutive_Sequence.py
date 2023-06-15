from typing import List

class Solution:
    def _uniq_sorted(self, nums):
        storage = []
        nums = sorted(nums)
        for n in nums:
            if n not in storage:
                storage.append(n)
        return storage
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = self._uniq_sorted(nums)
        index = 0
        print(nums)
        while index < len(nums):
            try:
                if nums[index+1] == nums[index] + 1:
                    pass
                else:
                    return index+1
            except:
                pass
            index += 1
        return len(nums)

if __name__ == '__main__':
    test_nums_1 = [100,4,200,1,3,2]
    test_nums_2 = [0,3,7,2,5,8,4,6,0,1]
    test_nums_3 = [9,1,4,7,3,-1,0,5,8,-1,6]
    sol = Solution()
    print(sol.longestConsecutive(nums=test_nums_3))