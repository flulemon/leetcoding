#### Three Sum
Link: https://leetcode.com/problems/3sum/

Given an array `nums` of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```
Example 2:
```
Input: nums = []
Output: []
```
Example 3:
```
Input: nums = [0]
Output: []
```

Constraints:
```
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
```


### Edge cases
- No elements in array must produce empty array solution
- If there are less than 3 items in array then there's no solution
- ` solution set must not contain duplicate triplets` - sort triplet before adding it to solution


### Solutions
#### Solution #1 (Brute force)
Time complexity: O(N^3)

Space complexity: O(1)

Explanation: iterate each triplet of elements in array and check if their sum equals to 0

#### Solution #2
Time complexity: O(N^2)

Space complexity: O(N)

Explanation: a + b + c = 0 -> a + b = -c, so we need to find two elements which sum is equal to -c, that is two sum task which can be completed in O(N) time and O(N) space.
But we need to do this to every item in array, therefore time complexity will be O(N^2).
