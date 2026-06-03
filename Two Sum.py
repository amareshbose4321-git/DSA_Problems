#--------------
# Two Sum
#--------------

# easy

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

# class Solution:
#     def twoSum(self, nums, target):

#         seen = {}

#         for i in range(len(nums)):

#             c = target - nums[i]

#             if c in seen:
#                 return (seen[c],i)
            
#             seen[nums[i]] = i

# obj = Solution()

# # Example 1:
# print(obj.twoSum([2,7,11,15],9))

# # Example 2:
# print(obj.twoSum([3,2,4],6))

# # Example 3:
# print(obj.twoSum([3,3],6))


# Time complexity : O(n)
# Space complexity : O(n)

#------------------------------------------------------


#-------------------------------------------------------
# 167. Two Sum II - Input Array Is Sorted (LeetCode)
#-------------------------------------------------------
# Medium

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 
# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000


# CODE
#----------------------------
# Two pointer method 
# It is use when it's given sorted array and we find indiex of a given sorted array or we find a value of given unsorted array to convert into sorted.
# But does not work for finding unsorted array index.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Two pointer method
        i = 0
        j = len(numbers)-1

        while i < j:
            sum = numbers[i] + numbers[j]

            if sum == target:
                return (i+1, j+1)
            elif sum < target:
                i+=1
            else:
                j-=1
                
#----------------------------------------------------

        # Hash method
        # seen = {}

        # for i in range(len(numbers)):
        #     c = target - numbers[i]

        #     if c in seen:
        #         return (seen[c]+1,i+1)
            
        #     seen[numbers[i]] = i


obj = Solution()

# Example 1:
print(obj.twoSum([2,7,11,15],9))

# Example 2:
print(obj.twoSum([2,3,4],6))

# Example 3:
print(obj.twoSum([-1,0],-1))

# Time complexity : O(n)
# Space complexity : O(1)

# Here hashmap is not good because it is a sorted array and also hash method time complexity is O(n) and  Space complexity  O(n) but in two pointer the time complexity is O(n) and  Space complexity  O(1). 
# We see less space required in two pointer 
# But when we use unsorted array/list and find index then we use hash method.