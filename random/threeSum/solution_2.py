from typing import List, Set, Tuple
from test_cases import BaseSolution


class Solution(BaseSolution):
    def solve(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        solutions: Set[Tuple[int]] = set()
        targets = {nums[i]: i for i in range(len(nums))}

        def add_solution(solution: List[int]):
            solutions.add(tuple(sorted(nums[ix] for ix in solution)))

        for target_value, target_index in targets.items():
            diffs = dict()
            for i in range(len(nums)):
                if i == target_index:
                    continue
                if nums[i] in diffs:
                    add_solution([i, diffs[nums[i]], target_index])
                else:
                    diffs[-1 * target_value - nums[i]] = i
        return [list(t) for t in solutions]


if __name__ == "__main__":
    Solution().run_tests()
