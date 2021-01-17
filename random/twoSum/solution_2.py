from typing import List
from test_cases import BaseSolution


class Solution(BaseSolution):
    def solve(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()
        for i in range(len(nums)):
            if nums[i] in diffs:
                return [i, diffs[nums[i]]]
            diffs[target - nums[i]] = i
        return [-1, -1]


if __name__ == "__main__":
    Solution().run_tests()
