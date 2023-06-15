from typing import List, Dict

class Solution:
	def _make_dict(self, nums: List[int]) -> Dict[int, int]:
		result = {}
		for i in nums:
			if i not in result.keys():
				result[i] = 1
			else:
				result[i] += 1

		return result

	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
	    by_quantity = self._make_dict(nums=nums)
	    result = []

	    sorted_values = sorted(list(by_quantity.values()))[-k:]
	    
	    for key, value in by_quantity.items():
	    	if value in sorted_values:
	    		result.append(key)

	    return result

    
if __name__ == '__main__':
	sol = Solution()

	test_list_1 = [1,1,1,2,2,3]
	test_k_1 = 2

	test_1 = sol.topKFrequent(nums=test_list_1, k=test_k_1)
	print(test_1)