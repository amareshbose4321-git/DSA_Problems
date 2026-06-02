#--------------
# Two Sum
#--------------

# Accepted  # easy

# Hints
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.



# CODE
#----------------------------------------------
# Using Hash Map (Dictionary) method. --> Optimal method
# In Python, a dictionary ({}) is implemented using a hash table, so:

class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            c = target - nums[i]

            if c in seen:
                return (seen[c],i)
            
            seen[nums[i]] = i

obj = Solution()

# Example 1:
print(obj.twoSum([2,7,11,15],9))

# Example 2:
print(obj.twoSum([3,2,4],6))

# Example 3:
print(obj.twoSum([3,3],6))

#------------------------------------------------------


# Two pointer method 
# It is use when it's given sorted array and we find indiex of a given sorted array or we find a value of given unsorted array to convert into sorted.
# But does not work for finding unsorted array index.

from numpy import *

class Solution:
    def twoSum(self,nums,target):
        
        i = 0
        j = len(nums)-1
        
        nums.sort()
        
        while(i < j):
            sum = nums[i] + nums[j]
            
            if sum > target:
                j-=1
            elif sum < target:
                i+=1
            else:
                return [int(i),int(j)]
        return None

              
obj = Solution()
print(obj.twoSum(array([2,7,11,5]),9))

