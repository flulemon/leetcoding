#### Two Sum
Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
Example 3:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

Constraints:

```
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
```
Only one valid answer exists.

### Solutions
#### Solution #1
Time complexity: O(N^2)

Space complexity: O(1)

Explanation: iterate each pair of elements in array and check if their sum equals to `target`

#### Solution #2
Time complexity: O(N) 

Space complexity: O(N)

Explanation: iterate array and save difference between element and `target` into dictionary as a key and element's index as value.
At each iteration also check if current element is in the dictionary. If it is, then return index from dictionary and current element index.