from typing import List
from dataclasses import dataclass


@dataclass
class TestCase:
    nums: List[int]
    target: int
    solution: List[int]


tests: List[TestCase] = [
    TestCase(nums=[2,7,11,15], target=9, solution=[0,1]),
    TestCase(nums=[3,2,4], target=6, solution=[1,2]),
    TestCase(nums=[3,3], target=6, solution=[0,1]),
]


class BaseSolution:
    def run_tests(self):
        for test in tests:
            print('-------------')
            solution, is_right = self.run_test(test)
            if is_right:
                print(f'Test accepted')
            else:
                print('Test failed')
                print(f'Expected: {test.solution}')
                print(f'Actual: {solution}')
                print(f'Test: {test}')

    def run_test(self, test: TestCase):
        solution = self.solve(test.nums, test.target)
        return solution, len(set(solution).difference(set(test.solution))) == 0

    def solve(self, nums: List[int], target: int) -> List[int]:
        raise NotImplementedError()
