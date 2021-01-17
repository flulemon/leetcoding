from typing import List, Set, Tuple
from test_cases import BaseSolution


# Brute force
class Solution(BaseSolution):
    def solve(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        solutions: Set[Tuple[int]] = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        solutions.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(t) for t in solutions]


if __name__ == "__main__":
    Solution().run_tests()
