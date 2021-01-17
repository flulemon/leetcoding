from typing import List
from dataclasses import dataclass


@dataclass
class TestCase:
    nums: List[int]
    solution: List[List[int]]


tests: List[TestCase] = [
    TestCase(nums=[-1,0,1,2,-1,-4], solution=[[-1,-1,2],[-1,0,1]]),
    TestCase(nums=[], solution=[]),
    TestCase(nums=[0], solution=[]),
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
        solution = self.solve(test.nums)
        actual_solution = set(tuple(triplet) for triplet in solution)
        test_solution = set(tuple(triplet) for triplet in test.solution)
        return solution, len(actual_solution.difference(test_solution)) == 0

    def solve(self, nums: List[int]) -> List[List[int]]:
        raise NotImplementedError()
