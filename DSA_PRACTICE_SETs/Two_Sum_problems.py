"""
Problem statements: -> 
Given an array of integers nums and an integer target,
 return the indices of the two numbers such that they add up to target.
"""

"""
Brute Force Solution: -> Check every possible pairs.

"""
"""
------------------------------------------------------
"""
def twoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return [i, j]
            
"""
-----------------------------------------------------------
"""

"""
Optimal solutions 
"""

def twoSum(nums, target):

    hashmap = {}

    for i, num in enumerate(nums):

        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[num] = i

"""
------------------------------------------------------------------------------
HashMap allows constant-time lookup of previously seen numbers, 
reducing the nested loop O(n²) approach into a single-pass O(n) solution.

"""

"""
best interview version :- 
"""
class Solution:
    def twoSum(self, nums, target):

        hashmap = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i


nums = [4,5,15,-7,8,5,8]
target = int(input("Enter the target : "))
sol = Solution()
result = sol.twoSum(nums,target)
print("The Result is : ", result)

